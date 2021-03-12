'''
Prod L	Description
========================================================================
FIT  2	EFI/FGM Onboard Spin Fit Level 2 CDF

FIT  1	EFI/FGM Onboard Spin Fit Level 1 CDF

FIT  0	EFI/FGM Onboard Spin Fit Level 0 Packets


'''
from . import _Fields
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
