import os

#try and find the THEMIS_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(os.path.abspath(__file__))
DataPath = os.getenv('THEMIS_PATH')
if DataPath is None:
	print('Please set THEMIS_PATH environment variable')
	DataPath = ''
else:
	DataPath = os.path.normpath(DataPath)

#THEMIS position
aPos = None
bPos = None
cPos = None
dPos = None
ePos = None
Vel = {}


#functions which will interpolate the positions/traces of each spacecraft
TraceFuncs = {}
