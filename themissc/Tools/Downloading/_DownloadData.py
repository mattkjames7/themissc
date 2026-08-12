from ... import Globals
import numpy as np
import DateTimeTools as TT
from ._GetCDFURL import _GetCDFURL
import os
import re
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests
from tqdm.auto import tqdm
from ._ReadDataIndex import _ReadDataIndex
from ._UpdateDataIndex import _UpdateDataIndex
import RecarrayTools as RT
from ._ExtractDateVersion import _ExtractDateVersion
from ._ReduceDownloadList import _ReduceDownloadList
from datetime import datetime

def _DownloadFile(url,outfname):
	'''Download one file atomically and return its output name.'''
	tmpfname = outfname+'.part'
	try:
		with requests.get(url,stream=True,timeout=(10,120)) as response:
			response.raise_for_status()
			with open(tmpfname,'wb') as f:
				for chunk in response.iter_content(chunk_size=1024*1024):
					if chunk:
						f.write(chunk)
		os.replace(tmpfname,outfname)
		return outfname
	except Exception:
		if os.path.isfile(tmpfname):
			os.remove(tmpfname)
		raise

def _DownloadData(URLF,fname,outpath,Date=[20070101,None],
				vfmt='v\d',FContains=None,Overwrite=False,
				Progress=False,Download=True):
	'''
	Downloads Arase data

	Inputs
	======
	url0 : function
		Base URL of the data repository
	fname : string
		Full path and file name of index file
	outpath : string
		Path to download the data to
	Date : int
		Date to download data for in format yyyymmdd
		If single date - only data from that one day will be fetched
		If 2-element array - dates from Date[0] to Date[1] will be downloaded
		If > 2 elements - this is treated as a specific list of dates to download
	vfmt : list
		2 element list containing characters which split the version
		numbers, by default	it is ['v','.']
	FContains : str or None
		if set to a string, only files which contain the given substring will be downloaded
	Overwrite : bool
		If True then existing files will be overwritten
	'''

	#check if the output path exists
	if not os.path.isdir(outpath):
		os.makedirs(outpath,exist_ok=True)

	#populate the list of dates to download
	if np.size(Date) == 1:
		dates = np.array([Date])
	elif np.size(Date) == 2:
		end_date = Date[1]
		if end_date is None:
			end_date = int(datetime.now().strftime("%Y%m%d"))
		dates = TT.ListDates(Date[0],end_date)
	else:
		dates = np.array([Date]).flatten()
	n = dates.size

	#get a list of base URLS to scan
	urls0 = np.zeros(n,dtype='object')
	for i in range(0,n):
		print('\rDetermining URLs, date {0} of {1}'.format(i+1,n),end='')
		urls0[i] = URLF(dates[i])
	print()

	#get the unique ones
	uurl0,inverse = np.unique(urls0,return_inverse=True)
	nu0 = np.size(uurl0)

	#create an array of cdf urls and file names
	urls = []
	fnames = []
	for i in range(0,nu0):
		print('\rScanning for CDF URLs {0} of {1}'.format(i+1,nu0),end='')
		#use = np.where(inverse == i)[0]
		_urls,_fnames = _GetCDFURL(uurl0[i])
		urls.append(_urls)
		fnames.append(_fnames)
	print()
	urls = np.concatenate(urls)
	fnames = np.concatenate(fnames)
	nu = urls.size

	if nu == 0:
		print('No CDF URLs found')
		return
	else:
		print('{:d} CDF URLs found'.format(nu))

	#find file name dates and versions
	print('Parsing file dates and versions')
	fDate,Ver = _ExtractDateVersion(fnames,vfmt)

	#reduce the lists
	idx = _ReadDataIndex(fname)
	urls,fnames,fDate,Ver = _ReduceDownloadList(urls,fnames,fDate,Ver,idx,dates,FContains,Overwrite)
	nu = urls.size

	if nu == 0:
		print('No files to download')
		return
	else:
		print('{:d} files to download'.format(nu))

	if Download == False:
		return fDate

	#create new output index
	new_idx = np.recarray(nu,dtype=idx.dtype)
	new_idx.Date[:] = -1

	# Download concurrently. Iterating over as_completed means that one slow
	# server response cannot hold up progress reporting for all other files.
	p = 0
	workers = min(8,nu)
	with ThreadPoolExecutor(max_workers=workers) as executor:
		futures = {
			executor.submit(_DownloadFile,urls[j],os.path.join(outpath,fnames[j])): j
			for j in range(0,nu)
		}
		for future in tqdm(as_completed(futures),total=nu,
				desc='Downloading CDF files',unit='file',disable=not Progress):
			j = futures[future]
			try:
				future.result()
			except Exception as err:
				tqdm.write('Failed to download {0}: {1}'.format(fnames[j],err))
				continue
			new_idx.Date[p] = fDate[j]
			new_idx.FileName[p] = fnames[j]
			new_idx.Version[p] = Ver[j]
			p+=1

	new_idx = new_idx[:p]


	#check for duplicates within old index
	usen = np.ones(p,dtype='bool')
	useo = np.ones(idx.size,dtype='bool')

	for j in range(0,p):
		match = np.where(idx.Date == new_idx.Date[j])[0]
		if match.size > 0:
			if idx.Version[match[0]] > new_idx.Version[j]:
				#old one is newer (unlikely)
				usen[j] = False
			else:
				#new one is newer
				useo[match[0]] = False

	usen = np.where(usen)[0]
	new_idx = new_idx[usen]
	useo = np.where(useo)[0]
	idx = idx[useo]

	#join indices together and update file
	idx_out = RT.JoinRecarray(idx,new_idx)
	srt = np.argsort(idx_out.Date)
	idx_out = idx_out[srt]
	_UpdateDataIndex(idx_out,fname)
