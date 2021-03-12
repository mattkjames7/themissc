import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _SCM
import os


def ReadCDF(Date,sc='a',Prod='SCM',L='2'):
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
	SCM  2	Search Coil Magnetometer Level 2 CDF

	SCF  1	Search Coil Magnetometer Fast Survey Level 1 CDF
	SCP  1	Search Coil Magnetometer Particle Burst Level 1 CDF
	SCW  1	Search Coil Magnetometer Wave Burst Level 1 CDF

	SCF  0	Search Coil Magnetometer Fast Survey Level 0 Packets
	SCP  0	Search Coil Magnetometer Particle Burst Level 0 Packets
	SCW  0	Search Coil Magnetometer Wave Burst Level 0 Packets

	(Level 0 data might not work)
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_SCM.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.SCM.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _SCM.datapath.format(Prod,L,sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
