import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _Pos
import os


def ReadCDF(Date,sc='a',Prod='V03',L='1'):
	'''
	Inputs
	======
	sc : str
		'a'|'b'|'c'|'d'|'e'
	Prod: str
		Product string (see below)
	L : str or int
		Level of data to download (0,1,2)




	Available data products
	=======================

	Prod L	Description
	========================================================================
	V00  1	Version 0 (Predicted Ephemeris Only) STATE L1 CDF
	V01  1	Version 1 (Predicted Ephemeris + spin model) Level 1 CDF
	V02  1	Version 2 (Definitive Ephemeris + spin) Level 1 CDF
	V03  1	Version 3 (Definitive Ephemeris + spin attitude corrections) Level 1 CDF

	(Level 0 data might not work)
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_Pos.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.Pos.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _Pos.datapath.format(Prod,L,sc) + idx[mx].FileName
	print(fname)

	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
