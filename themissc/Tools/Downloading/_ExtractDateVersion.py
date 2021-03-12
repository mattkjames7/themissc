import numpy as np
import re

def _ExtractDateVersion(files,vfmt='v\d'):
	'''
	extract dates and file versions for each file
	
	'''
	
	dp = re.compile('\d\d\d\d\d\d\d\d')
	vp = re.compile(vfmt)
	
	nf = np.size(files)
	Date = np.zeros(nf,dtype='int32')
	Ver = np.zeros(nf,dtype='int16')
	
	vlet = vfmt.replace('\d','')
	
	for i in range(0,nf):
		Date[i] = np.int32(dp.search(files[i]).group())
		tmp = vp.search(files[i]).group()
		for v in vlet:
			tmp = tmp.replace(v,'')
		Ver[i] = np.int32(tmp)
				
	return Date,Ver
