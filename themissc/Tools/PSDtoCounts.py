import numpy as np
from .PSDtoFlux import PSDtoFlux,PSDtoFluxE
from .FluxtoCounts import FluxtoCounts,FluxtoCountsE


def PSDtoCounts(v,f,m,Eff=1.0,dOmega=1.0,nSpec=1.0,Tau=1.0,g=1.0):
	'''
	Convert PSD to counts
	
	Inputs
	======
	v : float
		Speed, m/s
	f : float
		PSD
	m : float
		Particl mass, kg
		
	
	
	'''
	dJdE = PSDtoFlux(v,f,m)
	C = FluxtoCounts(v,dJdE,m,Eff,dOmega,nSpec,Tau,g)
	return C

def PSDtoCountsE(E,f,m,Eff=1.0,dOmega=1.0,nSpec=1.0,Tau=1.0,g=1.0):
	'''
	Convert PSD to counts
	
	Inputs
	======
	E : float
		Energy (keV)
	f : float
		PSD
	m : float
		Particl mass, kg
		
	
	
	'''
	dJdE = PSDtoFluxE(E,f,m)
	C = FluxtoCountsE(E,dJdE,m,Eff,dOmega,nSpec,Tau,g)
	return C
