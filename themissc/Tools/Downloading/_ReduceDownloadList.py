import numpy as np


def _ReduceDownloadList(urls,files,Date,Ver,idx,dates,FContains,Overwrite=False):
	'''
	'''
	
	nf = np.size(files)
	
	#get unique dates
	ud = np.unique(Date)
	
	keep = np.ones(nf,dtype='bool')

	#check if the file names contain a substring
	if not FContains is None:
		for i in range(0,nf):
			if not FContains in files[i]:
				keep[i] = False



	#remove multiple versions
	for i in range(0,ud.size):
		use = np.where((Date == ud[i]) & (keep))[0]
		if use.size > 1:
			bad = np.where(Ver[use] < np.max(Ver[use]))[0]
			keep[use[bad]] = False
			
	#now remove versions which exist
	if not Overwrite:
		for i in range(0,nf):
			if keep[i]:
				inidx = ((idx.Date == Date[i]) & (idx.Version == Ver[i])).any()
				if inidx:
					keep[i] = False
	

	
	#check which dates are in "dates"
	for i in range(0,nf):
		if not Date[i] in dates:
			keep[i] = False

	
	#reduce arrays
	use = np.where(keep)[0]
	
	urls = urls[use]
	files = files[use]
	Date = Date[use]
	Ver = Ver[use]
	
	return urls,files,Date,Ver
