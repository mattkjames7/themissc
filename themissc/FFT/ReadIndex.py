import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from . import _FFT

def ReadIndex(sc='a',Prod='FFT',L='2'):
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


	Prod   L	Description
	========================================================================
	FFT    2	Onboard FFT Level 2 CDF

	FFF_16 1	Onboard FFT Fast Survey 16 Bin Level 1 CDF
	FFF_32 1	Onboard FFT Fast Survey 32 Bin Level 1 CDF
	FFF_64 1	Onboard FFT Fast Survey 64 Bin Level 1 CDF
	FFP_16 1	Onboard FFT Particle Burst 16 Bin Level 1 CDF
	FFP_32 1	Onboard FFT Particle Burst 32 Bin Level 1 CDF
	FFP_64 1	Onboard FFT Particle Burst 64 Bin Level 1 CDF
	FFW_16 1	Onboard FFT Wave Burst 16 Bin Level 1 CDF
	FFW_32 1	Onboard FFT Wave Burst 32 Bin Level 1 CDF
	FFW_64 1	Onboard FFT Wave Burst 64 Bin Level 1 CDF

	FFF    0	Onboard FFT Fast Survey Level 0 Packets
	FFP    0	Onboard FFT Particle Burst Level 0 Packets
	FFW    0	Onboard FFT Wave Burst Level 0 Packets

	(Level 0 data might not work)
	
	
	Returns
	=======
	numpy.recarray
	
	'''
	return _ReadDataIndex(_FFT.idxfname.format(Prod,L,sc))
