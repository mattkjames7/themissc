'''
Prod   L	Description
========================================================================
FFT    2	Onboard FFT Level 2 CDF

FFF_16 1	Onboard FFT Fast Survey 16 Bin Level 1 CDF
FFF_32 1	Onboard FFT Fast Survey 32 Bin Level 1 CDF
FFF_64 1	Onboard FFT Fast Survey 64 Bin Level 1 CDF
FFP_16 1	Onboard FFT Particle Burst 16 Bin Level 1 CDF
FFP_32 1	Onboard FFT Particle Burst 32 Bin Level 1 CDF
FFP_64 1	Onboard FFT Particle Burst 64 Bin Level 1 CDF
FFW_16 1	Onboard FFT Wave Burst 16 Bin Level 1 CDF
FFW_32 1	Onboard FFT Wave Burst 32 Bin Level 1 CDF
FFW_64 1	Onboard FFT Wave Burst 64 Bin Level 1 CDF

FFF    0	Onboard FFT Fast Survey Level 0 Packets
FFP    0	Onboard FFT Particle Burst Level 0 Packets
FFW    0	Onboard FFT Wave Burst Level 0 Packets


'''
from . import _FFT
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
