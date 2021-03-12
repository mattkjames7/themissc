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
	SCM  2	Search Coil Magnetometer Level 2 CDF

	SCF  1	Search Coil Magnetometer Fast Survey Level 1 CDF
	SCP  1	Search Coil Magnetometer Particle Burst Level 1 CDF
	SCW  1	Search Coil Magnetometer Wave Burst Level 1 CDF

	SCF  0	Search Coil Magnetometer Fast Survey Level 0 Packets
	SCP  0	Search Coil Magnetometer Particle Burst Level 0 Packets
	SCW  0	Search Coil Magnetometer Wave Burst Level 0 Packets


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

