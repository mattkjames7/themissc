import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _MOM


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
	GMOM 2	Ground Moments Level 2 CDF

	(Level 0 data might not work)
	'''		
	idxfname = _MOM.idxfname.format(Prod,L,sc)
	datapath = _MOM.datapath.format(Prod,L,sc)

	vfmt = _MOM.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
