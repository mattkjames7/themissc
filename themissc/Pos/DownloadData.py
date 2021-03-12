from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _Pos
from .URL import URL

def DownloadData(sc='a',Prod='V03',L='1',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads ephemeris data.

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

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_Pos.idxfname.format(Prod,L,sc),_Pos.datapath.format(Prod,L,sc),
			Date,_Pos.vfmt,None,Overwrite,Verbose)
	
	
