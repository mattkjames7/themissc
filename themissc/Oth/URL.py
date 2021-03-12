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


	Not too sure what some of these products do, or whether they should be 
	attributed to another instrument in it's own submodule - file a bug
	report if something should be moved!

	Prod            L	Description
	========================================================================
	BAU             1	Bus Avionics Unit Housekeeping Level 1 CDF
	BAU Power       0	Bus Avionics Unit Power Housekeeping Level 0 Packets
	BAU Sun Sensor  0	Bus Avionics Unit Sun Sensor Housekeeping Level 0 Packets
	BAU UTC         0	BAU UTC Offset Level 0 Packets
	FBK             0	Onboard Filter Bank Level 0 Packets
	FBK             1	Filter Bank Level 1 CDF
	FBK             2	Filter Bank Level 2 CDF
	HSK             1	IDPU Housekeeping Level 1 CDF
	IDPU HSK 404    0	IDPU Housekeeping (404) L0 Packets
	IDPU HSK 406    0	IDPU Housekeeping (406) L0 Packets
	IDPU MEM        0	IDPU Memory Dump Packets
	TRG             0	IDPU Trigger Values L0 Packets
	TRG             1	IDPU FSW Burst Trigger Values Level 1 CDF
	SCMODE          1	Spacecraft mode (Slow Survey  Fast Survey Wave Burst  Particle Burst) L1 CDF


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

