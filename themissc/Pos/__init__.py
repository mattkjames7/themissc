'''

Prod L	Description
========================================================================
V00  1	Version 0 (Predicted Ephemeris Only) STATE L1 CDF
V01  1	Version 1 (Predicted Ephemeris + spin model) Level 1 CDF
V02  1	Version 2 (Definitive Ephemeris + spin) Level 1 CDF
V03  1	Version 3 (Definitive Ephemeris + spin attitude corrections) Level 1 CDF

V03 will be used by default

'''
from . import _Pos
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
