from .. import Globals 
import time
import os
import numpy as np

def URL(sc,Prod,L):
	'''
	Returns a function which works out the URLs for a given date
	
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
	urls
	'''
	
	def URLFunction(Date):
	
		#get the year
		Year = Date//10000
		
		#get the URL for that year
		url0 = 'http://themis.ssl.berkeley.edu/data/themis/th{:s}/l{:s}/{:s}/{:04d}/'.format(sc.lower(),str(L),Prod.lower(),Year)
		
		return url0
	
	return URLFunction

