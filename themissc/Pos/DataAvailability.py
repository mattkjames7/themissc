import numpy as np
from .ReadIndex import ReadIndex

def DataAvailability(sc='a',Prod='V03',L='1'):
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
	V00  1	Version 0 (Predicted Ephemeris Only) STATE L1 CDF
	V01  1	Version 1 (Predicted Ephemeris + spin model) Level 1 CDF
	V02  1	Version 2 (Definitive Ephemeris + spin) Level 1 CDF
	V03  1	Version 3 (Definitive Ephemeris + spin attitude corrections) Level 1 CDF

	(Level 0 data might not work)

	
	'''
	idx = ReadIndex(sc,Prod,L)
	return np.unique(idx.Date)
