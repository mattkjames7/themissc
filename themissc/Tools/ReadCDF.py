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
	
	#get the list of zVariables. cdflib >= 1.0 returns a CDFInfo
	#dataclass, while older releases returned a dictionary.
	info = f.cdf_info()
	if isinstance(info,dict):
		var = info['zVariables']
	else:
		var = info.zVariables
	
	#create ouput dicts
	data = {}
	attr = {}
	for v in var:
		try:
			data[v] = f.varget(v)
		except ValueError as err:
			# Current cdflib raises for variables which are defined in the
			# CDF but have no records. Preserve them in the output as empty.
			if 'No records found for variable' not in str(err):
				raise
			data[v] = np.array([])
		attr[v] = f.varattsget(v)

	#delete cdf (not sure if this is necessary - no idea if there is a close function)
	del f
	
	return data,attr
