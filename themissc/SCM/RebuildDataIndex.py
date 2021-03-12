import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _SCM


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
	idxfname = _SCM.idxfname.format(Prod,L,sc)
	datapath = _SCM.datapath.format(Prod,L,sc)

	vfmt = _SCM.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
