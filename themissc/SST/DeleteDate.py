import numpy as np
from ..Tools.Downloading._DeleteDate import _DeleteDate
from . import _SST

def DeleteDate(Date,sc,Prod,L,Confirm=True):
	'''
	delete all of the files from a given date
	
	'''
	idxfname = _SST.idxfname.format(Prod,L,sc)
	datapath = _SST.datapath.format(Prod,L,sc)

	_DeleteDate(Date,idxfname,datapath,Confirm)
