import numpy as np
from .RelVelocity import RelVelocity
from .RelEnergy import RelEnergy
from .PSDtoFlux import PSDtoFluxE
from scipy.optimize import minimize

kB = np.float64(1.38064852e-23)
e = np.float64(1.6022e-19)

def _MB_psd(E,n,T,m,CountConst=1.0):
	'''
	M-B dist outputting PSD
	
	'''
	#convert Energy to Joules
	Ej = E*1000*e
	
	#define the constant 
	A = n*(m/(2*np.pi*kB*T))**1.5
	
	#calculate the rest of the function
	f = A*np.exp(-Ej/(kB*T))

	return f

def _MB_psdv2(E,n,T,m,CountConst=1.0):
	'''
	M-B dist outputting PSD
	
	'''
	#convert Energy to Joules
	Ej = E*1000*e

	#define the constant 
	A = n*(m/(2*np.pi*kB*T))**1.5
	
	#calculate the psd
	f = A*np.exp(-Ej/(kB*T))

	#now velocity
	v = RelVelocity(E,m)

	return 4*np.pi*f*v**2

def _MB_psdv4(E,n,T,m,CountConst=1.0):
	'''
	M-B dist outputting PSD
	
	'''
	#convert Energy to Joules
	Ej = E*1000*e

	#define the constant 
	A = n*(m/(2*np.pi*kB*T))**1.5
	
	#calculate the psd
	f = A*np.exp(-Ej/(kB*T))

	#now velocity
	v = RelVelocity(E,m)

	return m*4*np.pi*f*v**4

def _MB_flux(E,n,T,m,CountConst=1.0):
	'''
	M-B dist outputting flux
	
	'''
	#convert Energy to Joules
	Ej = E*1000*e

	#define the constant 
	A = n*(m/(2*np.pi*kB*T))**1.5
	
	#calculate the psd
	f = A*np.exp(-Ej/(kB*T))
	
	#convert to flux
	flux = PSDtoFluxE(E,f,m)

	return flux
	
def _MB_cts(E,n,T,m,CountConst=1.0):
	'''
	M-B dist outputting flux
	
	'''
	#convert Energy to Joules
	Ej = E*1000*e

	#define the constant 
	A = n*(m/(2*np.pi*kB*T))**1.5
	
	#calculate the psd
	f = A*np.exp(-Ej/(kB*T))
	
	#convert to flux
	flux = PSDtoFluxE(E,f,m)
	
	#convert to counts
	cts = flux*E*CountConst
	
	return cts
	
def GetMaxwellianFunction(yparam):
	'''
	Return a function which will produce a M-B distribution.
	
	Inputs
	======
	yparam : str
		'Counts'|'Flux'|'PSD'|'PSD1D'|'PSD1Dv2' - this determines the
		output type
	
	'''
	funcs = {	'counts' : _MB_cts,
				'flux' : _MB_flux,
				'psd1d' : _MB_psdv2,
				'psd1dv2' : _MB_psdv4,
				'psd' : _MB_psd, }
	return funcs.get(yparam.lower(),funcs['psd'])

def Maxwellian(x,n,T,m,CountConst=1.0,xparam='V',yparam='PSD'):
	'''
	Given either velocity (m/s) or energy (keV) and a density/temperature
	calculate the Maxwell-Boltzmann distribution.
	
	Inputs
	======
	x : float
		Velocity in m/s or energy in keV
	n : float
		Density in m^-3 (not cm^-3)
	T : float
		Temperature in K
	m : float
		Particle mass (kg)
	Countconst : float
		Constant which can be used to convert between flux and counts
		using:
				Flux = Counts/(E*CountConst)
			i.e.
				CountConst = Counts/(E*Flux)
	xparam : str
		'V'|'E' - denotes whether the intput parameter is energy ('E')
		or velocity ('V')
	yparam : str
		'Counts'|'Flux'|'PSD'|'PSD1D'|'PSD1Dv2' - this determines the
		output type
		
	Returns
	=======
	f : float
		Distribution function in whichever type defined by "yparam"
	
	'''
	#get the energy
	if xparam == 'E':
		E = x
	else:
		E = RelEnergy(x,m)
	
	
	#determine which function to call
	Func = GetMaxwellianFunction(yparam)
	
	return Func(E,n,T,m,CountConst)

def _GetMisfitFunc(E,f,m,CountConst,MinFunc,MBFunc,LogDiff=True):
	'''
	Return a function which can be minimized.
	
	Inputs
	======
	E : float
		Energy in keV
	f : float
		the spectral data (whatever units defined by yparam)
	m : float
		Mass of particles in kg
	CountConst : float
		This is used if converting from flux to counts
	MinFunc : str
		'mean-squared'|'mean-abs'
	MBFunc : callable
		This will provide us with the MB dist
	LogDiff : bool
		If True, then the logarithm of the points will be taken prior to
		calculating the difference.
	'''
	lf = np.log10(f)
	
	def FuncMS(X):
		n,T = X 
		
		fm = MBFunc(E,n,T,m,CountConst)
		
		if LogDiff:
			lm = np.log10(fm)
			diff = np.sum(((lf-lm)**2))/f.size			
		else:
			diff = np.sum(((f-fm)**2))/f.size
		
		return diff
	
	def FuncMA(X):
		n,T = X 
		
		fm = MBFunc(E,n,T,m,CountConst)
		
		if LogDiff:
			lm = np.log10(fm)
			diff = np.sum(np.abs(lf-lm))/f.size			
		else:
			diff = np.sum(np.abs(f-fm)**2)/f.size
		
		return diff
	if MinFunc == 'mean-squared':
		return FuncMS
	else:
		return FuncMA


def FitMaxwellian(x,f,n0,T0,m,CountConst=1.0,xparam='V',yparam='PSD',
	Verbose=False,MaxIter=None,MinFunc='mean-squared',LogDiff=True,
	MinFit=3):

	#get the energy
	if xparam == 'E':
		E = x
	else:
		E = RelEnergy(x,m)

	#select only good data to fit to
	if yparam == 'Counts':
		goodf = np.isfinite(f) & (f >= 0)
	else:
		goodf = np.isfinite(f) & (f > 0)
	good = np.where(goodf)[0]
	if (good.size < MinFit):
		return -1, -1, False
		
	#get the MB function
	MBFunc = GetMaxwellianFunction(yparam)
	
	#get the misfit function to be minimized
	if np.size(CountConst) > 1:
		CC = CountConst[good]
	else:
		CC = CountConst
	Func = _GetMisfitFunc(E[good],f[good],m,CC,MinFunc,MBFunc,LogDiff)
	
	#set options
	if MaxIter is None:
		opt = {}
	else:
		opt = { 'maxiter' : MaxIter }
		
	#fit the function
	res = minimize(Func,[n0,T0],method='nelder-mead',options=opt)

	n,t = res.x
	if not res.success and Verbose:
		print('Warning - potentially bad M-B fit')
		print(res.message)
	return n,t,res.success
