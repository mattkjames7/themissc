import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from . import _Fields

def ReadIndex(sc='a',Prod='FIT',L='2'):
	'''
	Reads the index file for a given data product.
	
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
	
	
	Returns
	=======
	numpy.recarray
	
	'''
	return _ReadDataIndex(_Fields.idxfname.format(Prod,L,sc))
