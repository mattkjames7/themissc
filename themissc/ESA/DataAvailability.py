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
	MOM  2	Particle Moments Level 2 CDF
	ESA  2	Electrostatic Analyzer Level 2 CDF

	MOM  1	Onboard Particle Moments Level 1 CDF
	ESA  1	Electrostatic Analyzer Level 1 CDF

	MOM  0	Onboard Particle Moments Level 0 Packets
	EEB  0	ESA Electron Burst Distribution Level 0 Packets
	EEF  0	ESA Electron Full Distribution Level 0 Packets
	EER  0	ESA Electron Reduced Distribution Level 0 Packets
	EIB  0	ESA Ion Burst Distribution Level 0 Packets
	EIF  0	ESA Ion Full Distribution Level 0 Packets
	EIR  0	ESA Ion Reduced Distribution Level 0 Packets


	(Level 0 data might not work)

	
	'''
	idx = ReadIndex(sc,Prod,L)
	return np.unique(idx.Date)
