import numpy as np
from .CountstoFlux import CountstoFlux,CountstoFluxE
from .FluxtoPSD import FluxtoPSD,FluxtoPSDE


def CountstoPSD(v,C,m,Eff=1.0,dOmega=1.0,nSpec=1.0,Tau=1.0,g=1.0):
	'''
	Convert Counts to PSD
	
	Inputs
	======
	v : float
		Velocity, m/s
	C : float
		particle counts
	m : float
		particle mass, kg
	
	
	'''
	
	dJdE = CountstoFlux(v,C,m,Eff,dOmega,nSpec,Tau,g)
	f = FluxtoPSD(v,dJdE,m)
	
	return f

def CountstoPSDE(E,C,m,Eff=1.0,dOmega=1.0,nSpec=1.0,Tau=1.0,g=1.0):
	'''
	Convert Counts to PSD
	
	Inputs
	======
	E : float
		Energy (keV)
	C : float
		particle counts
	m : float
		particle mass, kg
	
	
	'''
	
	dJdE = CountstoFluxE(E,C,m,Eff,dOmega,nSpec,Tau,g)
	f = FluxtoPSDE(E,dJdE,m)
	
	return f
