from ... import Globals
import numpy as np
import DateTimeTools as TT
from ._GetCDFURL import _GetCDFURL
import os
import re
from ._ReadDataIndex import _ReadDataIndex
from ._UpdateDataIndex import _UpdateDataIndex
import RecarrayTools as RT
from ._ExtractDateVersion import _ExtractDateVersion
from ._ReduceDownloadList import _ReduceDownloadList

def _DownloadData(URLF,fname,outpath,Date=[20070101,20210101],
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
		os.system('mkdir -pv '+outpath)
	
	#populate the list of dates to download
	if np.size(Date) == 1:
		dates = np.array([Date])
	elif np.size(Date) == 2:
		dates = TT.ListDates(Date[0],Date[1])
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

	#start downloading files
	p = 0
	for j in range(0,nu):
		print('Downloading file {0} of {1} ({2})'.format(j+1,nu,fnames[j]))

		if Progress:
			os.system('wget '+urls[j]+' -O '+outpath+fnames[j])
		else:
			os.system('wget --no-verbose '+urls[j]+' -O '+outpath+fnames[j])
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

