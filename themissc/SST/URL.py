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

	Prod  L	Description
	========================================================================
	SST   2	Solid State Telescope Level 2 CDF

	SST   1	Solid State Telescope Level 1 CDF

	SEB   0	SST Electron Burst Distribution Level 0 Packets
	SEF   0	SST Electron Full Distribution Level 0 Packets
	SER   0	SST Electron Reduced Distribution Level 0 Packets
	SIB   0	SST Ion Burst Distribution Level 0 Packets
	SIF   0	SST Ion Full Distribution Level 0 Packets
	SIR   0	SST Ion Reduced Distribution Level 0 Packets
	SSTHK 0	SST Housekeeping L0 Packets


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

