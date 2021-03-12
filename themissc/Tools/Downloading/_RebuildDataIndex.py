import numpy as np
from ..ListFiles import ListFiles
import re
from ._UpdateDataIndex import _UpdateDataIndex

def _RebuildDataIndex(fpath,fname,vfmt='v\d\d'):
	
	#define the dtype
	dtype = [('Date','int32'),('FileName','object'),('Version','int32')]
	
	#list all of the files in the path
	_,files = ListFiles(fpath,ReturnNames=True)
	nf = files.size

	#create output array
	data = np.recarray(nf,dtype=dtype)
	
	#extract the versions from each file
	dp = re.compile('\d\d\d\d\d\d\d\d')
	vp = re.compile(vfmt)
	p = 0
	
	vlet = vfmt.replace('\d','')
	
	for i in range(0,nf):
		if '.cdf' in files[i]:
			print(files[i])
			Date = np.int32(dp.search(files[i]).group())
			try:
				tmp	= vp.search(files[i]).group()[1:]
				for v in vlet:
					tmp = tmp.replace(v,'')			
				Ver = np.int32(tmp)
			except:
				Ver = 0
			data.FileName[i] = files[i]
			data.Date[i] = Date
			data.Version[i] = Ver
			p += 1
	
	data = data[:p]
	
	#save data index
	_UpdateDataIndex(data,fname)
