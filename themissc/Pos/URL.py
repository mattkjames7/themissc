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
	V00  1	Version 0 (Predicted Ephemeris Only) STATE L1 CDF
	V01  1	Version 1 (Predicted Ephemeris + spin model) Level 1 CDF
	V02  1	Version 2 (Definitive Ephemeris + spin) Level 1 CDF
	V03  1	Version 3 (Definitive Ephemeris + spin attitude corrections) Level 1 CDF


	(Level 0 data might not work)


	Returns
	=======
	urls
	'''
	
	def URLFunction(Date):
	
		#get the year
		Year = Date//10000
		
		#get the URL for that year
		url0 = 'http://themis.ssl.berkeley.edu/data/themis/th{:s}/l{:s}/state/{:04d}/'.format(sc.lower(),str(L),Year)
		
		return url0
	
	return URLFunction

