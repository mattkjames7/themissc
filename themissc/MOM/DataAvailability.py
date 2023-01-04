import numpy as np
from .ReadIndex import ReadIndex

def DataAvailability(sc='a',Prod='MOM',L='2'):
	'''
	Provide a list of dates for which there are data.

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
	idx = ReadIndex(sc,Prod,L)
	return np.unique(idx.Date)
