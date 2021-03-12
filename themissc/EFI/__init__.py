'''

Prod L	Description
========================================================================
EFI  2	Electric Field Instrument Level 2 CDF

VAF  1	EFI Sensor Voltages A Fast Survey Level 1 CDF
VAP  1	EFI Sensor Voltages A Particle Burst Level 1 CDF
VAW  1	EFI Sensor Voltages A Wave Burst Level 1 CDF
VBF  1	EFI Sensor Voltages B Fast Survey Level 1 CDF
VBP  1	EFI Sensor Voltages B Particle Burst Level 1 CDF
VBW  1	EFI Sensor Voltages B Wave Burst Level 1 CDF
EFF  1	EFI Fast Survey Level 1 CDF
EFP  1	EFI Particle Burst Level 1 CDF
EFW  1	EFI Wave Burst Level 1 CDF

VAF  0	EFI Sensor Voltages A Fast Survey Level 0 Packets
VAP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
VAW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
VBF  0	EFI Sensor Voltages B Fast Survey Level 0 Packets
VBP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
VBW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
EFF  0	EFI E-field Fast Survey Level 0 Packets
EFP  0	EFI E-field Particle Burst Level 0 Packets
EFW  0	EFI E-field Wave Burst Level 0 Packets






'''
from . import _EFI
from .DownloadData import DownloadData
from .URL import URL
from .DataAvailability import DataAvailability
from .DeleteDate import DeleteDate
from .ReadCDF import ReadCDF
from .ReadIndex import ReadIndex
from .RebuildDataIndex import RebuildDataIndex
