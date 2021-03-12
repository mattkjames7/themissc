import numpy as np
from ._ReadDataIndex import _ReadDataIndex
from ._UpdateDataIndex import _UpdateDataIndex
import os

def _DeleteDate(Date,fname,path,Confirm=True):
	
	'''
	Delete a single day of data for an instrument
	
	Inputs
	======
	Date : int
		Integer date in format yyyymmdd
	fname : str
		Full name and path of index file
	path : str
		Path to data product
	Confirm : bool
		Confirm whether to delete each file before deleting
	
	'''
	
	#read the index
	idx = _ReadDataIndex(fname)


	#find the indices where the dates match the date to be deleted
	idel = np.where(idx.Date == Date)[0]
	if idel.size == 0:
		print('No files found for the date {:d}'.format(Date))
		return
		
	#loop through each on deleting the files
	ndel = idel.size
	removed = np.zeros(idx.size,dtype='bool')
	for i in range(0,ndel):
		inpt = 'y'
		if Confirm:
			inpt = input('Delete the file {:s}? (y/n):\n'.format(idx.FileName[idel[i]]))
		if inpt:
			os.system('rm -v '+path+idx.FileName[idel[i]])
			removed[idel[i]] = True
			
	#keep the remaining entries
	ikeep = np.where(removed == False)[0]
	idx = idx[ikeep]
	
	#update index file
	_UpdateDataIndex(idx,fname)
