import os 
import PyFileIO as pf

def _UpdateDataIndex(idx,fname):
	'''
	Updates the data index file.
	
	Input:
		idx: numpy.recarray containing the file names.
	'''
	
	pf.WriteASCIIData(fname,idx)
