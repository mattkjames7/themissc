from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _SCM
from .URL import URL

def DownloadData(sc='a',Prod='SCM',L='2',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads SCM data.

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

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_SCM.idxfname.format(Prod,L,sc),_SCM.datapath.format(Prod,L,sc),
			Date,_SCM.vfmt,None,Overwrite,Verbose)
	
	
