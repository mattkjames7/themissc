import numpy as np
from .RelVelocity import RelVelocity
from .RelEnergy import RelEnergy

def IntegrateSpectra(E,E0,E1,Flux,m,Omega,Vsc,Vbulk,Erange=(0.0,np.inf),nmin=3):
	'''
	Integrate fluxes in units of (keV sr cm^2 s)^-1 to calculate the 
	density, pressure and temperature in units of m^-3, Pa and K,
	repsectively.
	
	Inputs
	======
	E : float
		1D or 2D array of energy (must match dimensions of E0, E1 and
		Flux), where E is the energy of the centre of the bin (keV).
	E0 : float
		Lower bound of the energy bin (keV).
	E1 : float
		Upper bound of the energy bin (keV).
	Flux : float
		Measured differential number flux.
	m : float
		Particle mass in kg.
	Omega : float
		Solid angle (4*pi for HOPE)
	Vsc : float
		Array of spacecraft potentials to adjust energies by.
	Vbulk : float
		Bulk velocity relative to the spacecraft (actually speed, as
		Vbulk = |u_sc - v_ExB|) - provide me in m/s.
	Erange : tuple
		(min,max) tuple of the minimum and maximum energies to integrate 
		spectra over (keV), by default Erange=(0.0,np.inf).
	
	Returns
	=======
	n : float
		Density in SI units (m^-3).
	T : float
		Temperature (K).
	p : float
		Pressure (Pa).
	
	
	'''
	#constants
	kB = np.float64(1.38064852e-23)
	e = np.float64(1.6022e-19)
	
	#convert everything to 2D arrays, if it isn't already
	if len(np.shape(E)) == 1:
		E = np.array([E])
	if len(np.shape(E0)) == 1:
		E0 = np.array([E0])
	if len(np.shape(E1)) == 1:
		E1 = np.array([E1])
	if len(np.shape(Flux)) == 1:
		Flux = np.array([Flux])
		
	if (np.size(Vsc) != 1) and (len(np.shape(Vsc))) == 1:
		Vsc = np.array([Vsc]).T
	if (np.size(Vbulk) != 1) and (len(np.shape(Vbulk))) == 1:
		Vbulk = np.array([Vbulk]).T
		
	#calculate the effective energy by subtracting the spacecraft potential
	# and then subtracting the affect of the bulk velocity - convert to joules
	Vsck = Vsc/1000.0
	Ve = RelVelocity(E+Vsck,m) - Vbulk
	Ve0 = RelVelocity(E0+Vsck,m) - Vbulk
	Ve1 = RelVelocity(E1+Vsck,m) - Vbulk
	Ea = RelEnergy(Ve + Vbulk,m)*1000.0*e
	Ea0 = RelEnergy(Ve0 + Vbulk,m)*1000.0*e
	Ea1 = RelEnergy(Ve1 + Vbulk,m)*1000.0*e
	
	#convert Erange to joules from keV
	Er = np.array(Erange)*e*1000.0
	
	#calculate the width of the energy bin
	Emid = 0.5*(E0 + E1)*e*1000.0
	dEE = np.float64((E1-E0)/E)
	
	#convert Flux to SI units
	J = Flux*10.0 # times 10,000 to convert cm^-2 to m^-2, divide by 1000 for keV^-1 to eV^-1
	J = J/e # divide by electron charge to go from eV^-1 to J^-1
	
	#now both sets of sums
	Sn = np.zeros(J.shape[0],dtype='float32') + np.nan
	Sp = np.zeros(J.shape[0],dtype='float32') + np.nan
	for i in range(0,J.shape[0]):
		use = np.where((Emid[i] >= Er[0]) & (Emid[i] <= Er[1]))[0]
		if use.size > nmin:
			Sn[i] = np.sum(np.sqrt(Ea[i][use])*dEE[i][use]*np.float64(J[i][use]))
			Sp[i] = np.sum((Ea[i][use]**1.5)*dEE[i][use]*np.float64(J[i][use]))
	
	#calculate density (m^-3)
	n = Omega*np.sqrt(m/2)*Sn
	
	#and pressure (Pa)
	p = 2*Omega*np.sqrt(m/2)*Sp/3.0
	
	#now calculate temperature (K)
	T = p/(kB*n)
	
	return n,T,p
