import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _FGM


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
	FGM  2	Fluxgate Magnetometer Level 2 CDF

	FGM  1	Fluxgate Magnetometer Level 1 CDF

	FGE  0	Fluxgate Magnetometer Engineering Rate L0 Packets
	FGH  0	Fluxgate Magnetometer High Rate Level 0 Packets
	FGL  0	Fluxgate Magnetometer Low Rate Level 0 Packets


	(Level 0 data might not work)
	'''		
	idxfname = _FGM.idxfname.format(Prod,L,sc)
	datapath = _FGM.datapath.format(Prod,L,sc)

	vfmt = _FGM.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
