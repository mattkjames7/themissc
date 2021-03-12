import numpy as np
from ..Tools.Downloading._DeleteDate import _DeleteDate
from . import _Fields

def DeleteDate(Date,sc,Prod,L,Confirm=True):
	'''
	delete all of the files from a given date
	
	'''
	idxfname = _Fields.idxfname.format(Prod,L,sc)
	datapath = _Fields.datapath.format(Prod,L,sc)

	_DeleteDate(Date,idxfname,datapath,Confirm)
