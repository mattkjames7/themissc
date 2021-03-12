import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from . import _GMOM

def ReadIndex(sc='a',Prod='GMOM',L='2'):
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
	GMOM 2	Ground Moments Level 2 CDF

	(Level 0 data might not work)
	
	
	Returns
	=======
	numpy.recarray
	
	'''
	return _ReadDataIndex(_GMOM.idxfname.format(Prod,L,sc))
