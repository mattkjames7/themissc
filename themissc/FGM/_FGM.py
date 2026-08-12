import numpy as np
import os
from .. import Globals

#this just stores a few variables for this particular instrument

#data path and index file name: format(Prod,L,sc)
idxfname = os.path.join(Globals.DataPath,'FGM','{:s}.{:s}.{:s}.dat')
datapath = os.path.join(Globals.DataPath,'FGM','{:s}','{:s}','{:s}')

#file version format
vfmt = 'v\d\d'
