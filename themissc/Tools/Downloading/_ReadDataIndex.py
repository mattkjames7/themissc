import numpy as np
import PyFileIO as pf
import os

def _ReadDataIndex(fname):
	'''
	Reads index file containing a list of all of the dates with their
	associated data file name (so that we can pick the version 
	automatically).
	'''
	#define the dtype
	dtype = [('Date','int32'),('FileName','object'),('Version','int32')]
	
	
	#check it exists
	if not os.path.isfile(fname):
		return np.recarray(0,dtype=dtype)
		
	#read the index file
	try:
		data = pf.ReadASCIIData(fname,True,dtype=dtype)
	except:
		return np.recarray(0,dtype=dtype)
		
	return data
