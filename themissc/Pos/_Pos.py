import numpy as np
from .. import Globals

#this just stores a few variables for this particular instrument

#data path and index file name: format(Prod,L,sc)
idxfname = Globals.DataPath + 'Pos/{:s}.{:s}.{:s}.dat'
datapath = Globals.DataPath + 'Pos/{:s}/{:s}/{:s}/'

#file version format
vfmt = 'v\d'
