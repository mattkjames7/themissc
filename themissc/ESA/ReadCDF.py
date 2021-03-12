import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _ESA
import os


def ReadCDF(Date,sc='a',Prod='MOM',L='2'):
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
	MOM  2	Particle Moments Level 2 CDF
	ESA  2	Electrostatic Analyzer Level 2 CDF

	MOM  1	Onboard Particle Moments Level 1 CDF
	ESA  1	Electrostatic Analyzer Level 1 CDF

	MOM  0	Onboard Particle Moments Level 0 Packets
	EEB  0	ESA Electron Burst Distribution Level 0 Packets
	EEF  0	ESA Electron Full Distribution Level 0 Packets
	EER  0	ESA Electron Reduced Distribution Level 0 Packets
	EIB  0	ESA Ion Burst Distribution Level 0 Packets
	EIF  0	ESA Ion Full Distribution Level 0 Packets
	EIR  0	ESA Ion Reduced Distribution Level 0 Packets


	(Level 0 data might not work)
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_ESA.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.ESA.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _ESA.datapath.format(Prod,L,sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
