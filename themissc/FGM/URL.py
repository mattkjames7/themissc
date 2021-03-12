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


	Prod L	Description
	========================================================================
	FGM  2	Fluxgate Magnetometer Level 2 CDF

	FGM  1	Fluxgate Magnetometer Level 1 CDF

	FGE  0	Fluxgate Magnetometer Engineering Rate L0 Packets
	FGH  0	Fluxgate Magnetometer High Rate Level 0 Packets
	FGL  0	Fluxgate Magnetometer Low Rate Level 0 Packets

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

