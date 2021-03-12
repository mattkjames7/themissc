import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _Oth


def RebuildDataIndex(sc,Prod,L):
	'''
	Rebuilds the data index for a data product.

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
	idxfname = _Oth.idxfname.format(Prod,L,sc)
	datapath = _Oth.datapath.format(Prod,L,sc)

	vfmt = _Oth.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
