from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _FGM
from .URL import URL

def DownloadData(sc='a',Prod='FGM',L='2',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads FGM data.

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

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_FGM.idxfname.format(Prod,L,sc),_FGM.datapath.format(Prod,L,sc),
			Date,_FGM.vfmt,None,Overwrite,Verbose)
	
	
