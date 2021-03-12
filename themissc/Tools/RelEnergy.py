import numpy as np



def RelEnergy(v,m):
	'''
	Calculate the relativistic energy of a particle (hopefully correctly).
	
	Inputs
	======
	v : float
		velocity in m/s
	m : float 
		mass of particle in kg
		
	Returns
	=======
	K : float
		Energy in keV
	
	'''
	

	#calculate the energy in J
	c = np.float64(3e8)
	c2 = c**2
	mc2 = np.float64(m)*c2
	gamma = 1.0/np.sqrt(1-(np.float64(v**2)/c2))
	E = (gamma - 1.0)*mc2
	
	#convert to keV
	e = np.float64(1.6022e-19)
	K = (E/e)/1000.0
	
	return K
