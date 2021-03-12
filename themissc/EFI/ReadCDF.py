import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _EFI
import os


def ReadCDF(Date,sc='a',Prod='EFI',L='2'):
	'''
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
	
	'''
	
	#read the data index
	idx = _ReadDataIndex(_EFI.idxfname.format(Prod,L,sc))
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run themissc.EFI.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _EFI.datapath.format(Prod,L,sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
