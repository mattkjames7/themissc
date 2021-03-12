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
	EFI  2	Electric Field Instrument Level 2 CDF

	VAF  1	EFI Sensor Voltages A Fast Survey Level 1 CDF
	VAP  1	EFI Sensor Voltages A Particle Burst Level 1 CDF
	VAW  1	EFI Sensor Voltages A Wave Burst Level 1 CDF
	VBF  1	EFI Sensor Voltages B Fast Survey Level 1 CDF
	VBP  1	EFI Sensor Voltages B Particle Burst Level 1 CDF
	VBW  1	EFI Sensor Voltages B Wave Burst Level 1 CDF
	EFF  1	EFI Fast Survey Level 1 CDF
	EFP  1	EFI Particle Burst Level 1 CDF
	EFW  1	EFI Wave Burst Level 1 CDF

	VAF  0	EFI Sensor Voltages A Fast Survey Level 0 Packets
	VAP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
	VAW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
	VBF  0	EFI Sensor Voltages B Fast Survey Level 0 Packets
	VBP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
	VBW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
	EFF  0	EFI E-field Fast Survey Level 0 Packets
	EFP  0	EFI E-field Particle Burst Level 0 Packets
	EFW  0	EFI E-field Wave Burst Level 0 Packets

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

