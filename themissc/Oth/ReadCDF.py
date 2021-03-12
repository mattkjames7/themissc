import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _Oth
import os


def ReadCDF(Date,sc,Prod,L):
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


	Not too sure what some of these products do, or whether they should be 
	attributed to another instrument in it's own submodule - file a bug
	report if something should be moved!

	Prod            L	Description
	========================================================================
	BAU             1	Bus Avionics Unit Housekeeping Level 1 CDF
	BAU Power       0	Bus Avionics Unit Power Housekeeping Level 0 Packets
	BAU Sun Sensor  0	Bus Avionics Unit Sun Sensor Housekeeping Level 0 Packets
	BAU UTC         0	BAU UTC Offset Level 0 Packets
	FBK             0	Onboard Filter Bank Level 0 Packets
	FBK             1	Filter Bank Level 1 CDF
	FBK             2	Filter Bank Level 2 CDF
	HSK             1	IDPU Housekeeping Level 1 CDF
	IDPU HSK 404    0	IDPU Housekeeping (404) L0 Packets
	IDPU HSK 406    0	IDPU Housekeeping (406) L0 Packets
	IDPU MEM        0	IDPU Memory Dump Packets
	TRG             0	IDPU Trigger Values L0 Packets
	TRG             1	IDPU FSW Burst Trigger Values Level 1 CDF
	SCMODE          1	Spacecraft mode (Slow Survey  Fast Survey Wave Burst  Particle Burst) L1 CDF
	(Level 0 data might not work)
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_Oth.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.Oth.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _Oth.datapath.format(Prod,L,sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
