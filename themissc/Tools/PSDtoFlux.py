import numpy as np

def PSDtoFlux(v,f,m):
	'''
	Convert Flux to PSD
	
	Inputs
	======
	v : float
		Speed, m/s
	f : float
		PSD
	m : float
		Particl mass, kg
	
	'''
	e = 1.6022e-19
	
	return np.float64(np.float64(v**2)/m) * np.float64(e/10.0) * np.float64(f)

def PSDtoFluxE(E,f,m):
	'''
	Convert Flux to PSD
	
	Inputs
	======
	E : float
		Energy (keV)
	f : float
		PSD
	m : float
		Particl mass, kg
	
	'''
	e = 1.6022e-19
	K = E*e*1000.0
	return np.float64(np.float64(2*K)/(m**2)) * np.float64(e/10.0) * np.float64(f)
