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

