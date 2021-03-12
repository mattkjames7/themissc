import os

#try and find the THEMIS_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('THEMIS_PATH')+'/'
except:
	print('Please set THEMIS_PATH environment variable')
	DataPath = ''

#THEMIS position
aPos = None
bPos = None
cPos = None
dPos = None
ePos = None
Vel = {}


#functions which will interpolate the positions/traces of each spacecraft
TraceFuncs = {}
