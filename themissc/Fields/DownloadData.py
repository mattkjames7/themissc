from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _Fields
from .URL import URL

def DownloadData(sc='a',Prod='FIT',L='2',Date=[20070101,20210101],Overwrite=False,Verbose=True):
	'''
	Downloads Fields data.

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
	FIT  2	EFI/FGM Onboard Spin Fit Level 2 CDF

	FIT  1	EFI/FGM Onboard Spin Fit Level 1 CDF

	FIT  0	EFI/FGM Onboard Spin Fit Level 0 Packets


	(Level 0 data might not work)

	'''
	URLF = URL(sc,Prod,L)
	_DownloadData(URLF,_Fields.idxfname.format(Prod,L,sc),_Fields.datapath.format(Prod,L,sc),
			Date,_Fields.vfmt,None,Overwrite,Verbose)
	
	
