import numpy as np
import cdflib
import os

def ReadCDF(fname,Verbose=True):
	'''
	Read a CDF file contents
	'''
	
	if not os.path.isfile(fname):
		print('File not found')
		return None,None
	
	#open the file
	f = cdflib.CDF(fname)
	
	#get the list of zVariables
	var = f.cdf_info()['zVariables']
	
	#create ouput dicts
	data = {}
	attr = {}
	for v in var:
		data[v] = f.varget(v)
		attr[v] = f.varattsget(v)

	#delete cdf (not sure if this is necessary - no idea if there is a close function)
	del f
	
	return data,attr
