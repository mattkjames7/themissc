from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _SST
from .URL import URL

def DownloadData(sc='a',Prod='SST',L='2',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads SST data.

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

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_SST.idxfname.format(Prod,L,sc),_SST.datapath.format(Prod,L,sc),
			Date,_SST.vfmt,None,Overwrite,Verbose)
	
	
