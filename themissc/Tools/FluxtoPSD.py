import numpy as np


def FluxtoPSD(v,dJdE,m):
	'''
	Convert Flux to PSD
	
	Inputs
	======
	v : float
		Speed, m/s
	dJdE : float
		Flux
	m : float
		Particl mass, kg
	
	'''
	e = 1.6022e-19
	
	return np.float64(m/np.float64(v**2)) * np.float64(10.0/e) * np.float64(dJdE)

def FluxtoPSDE(E,dJdE,m):
	'''
	Convert Flux to PSD
	
	Inputs
	======
	E : float
		Energy (keV)
	dJdE : float
		Flux
	m : float
		Particl mass, kg
	
	'''
	e = 1.6022e-19
	K = E*e*1000.0
	#return np.float64(m**2/np.float64(2*K)) * np.float64(10.0/e) * np.float64(dJdE)
	return np.float64(m/(2*E)) * np.float64(dJdE)
