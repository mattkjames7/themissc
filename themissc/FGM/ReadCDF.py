import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _FGM
import os


def ReadCDF(Date,sc='a',Prod='FGM',L='2'):
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
	FGM  2	Fluxgate Magnetometer Level 2 CDF

	FGM  1	Fluxgate Magnetometer Level 1 CDF

	FGE  0	Fluxgate Magnetometer Engineering Rate L0 Packets
	FGH  0	Fluxgate Magnetometer High Rate Level 0 Packets
	FGL  0	Fluxgate Magnetometer Low Rate Level 0 Packets


	(Level 0 data might not work)
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_FGM.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.FGM.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _FGM.datapath.format(Prod,L,sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
