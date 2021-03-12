import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _Fields


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
	FIT  2	EFI/FGM Onboard Spin Fit Level 2 CDF

	FIT  1	EFI/FGM Onboard Spin Fit Level 1 CDF

	FIT  0	EFI/FGM Onboard Spin Fit Level 0 Packets


	(Level 0 data might not work)
	'''		
	idxfname = _Fields.idxfname.format(Prod,L,sc)
	datapath = _Fields.datapath.format(Prod,L,sc)

	vfmt = _Fields.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
