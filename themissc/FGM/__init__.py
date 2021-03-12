'''
Prod L	Description
========================================================================
FGM  2	Fluxgate Magnetometer Level 2 CDF

FGM  1	Fluxgate Magnetometer Level 1 CDF

FGE  0	Fluxgate Magnetometer Engineering Rate L0 Packets
FGH  0	Fluxgate Magnetometer High Rate Level 0 Packets
FGL  0	Fluxgate Magnetometer Low Rate Level 0 Packets

'''
from . import _FGM
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
