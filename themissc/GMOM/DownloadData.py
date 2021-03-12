from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _GMOM
from .URL import URL

def DownloadData(sc='a',Prod='GMOM',L='2',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads GMOM data.

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
	GMOM 2	Ground Moments Level 2 CDF

	(Level 0 data might not work)

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_GMOM.idxfname.format(Prod,L,sc),_GMOM.datapath.format(Prod,L,sc),
			Date,_GMOM.vfmt,None,Overwrite,Verbose)
	
	
