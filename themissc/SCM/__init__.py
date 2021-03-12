'''
Prod L	Description
========================================================================
SCM  2	Search Coil Magnetometer Level 2 CDF

SCF  1	Search Coil Magnetometer Fast Survey Level 1 CDF
SCP  1	Search Coil Magnetometer Particle Burst Level 1 CDF
SCW  1	Search Coil Magnetometer Wave Burst Level 1 CDF

SCF  0	Search Coil Magnetometer Fast Survey Level 0 Packets
SCP  0	Search Coil Magnetometer Particle Burst Level 0 Packets
SCW  0	Search Coil Magnetometer Wave Burst Level 0 Packets


'''
from . import _SCM
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
