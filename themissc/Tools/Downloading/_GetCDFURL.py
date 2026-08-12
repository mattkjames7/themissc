import numpy as np
import requests
from urllib.parse import urljoin

def _GetCDFURL(url0):
	'''
	Retrieves the url(s) of the cdf file to be downloaded.
	
	Inputs:
		Year: year
		Month: month
	Returns:
		urls,fnames
	'''
	
	# Fetch the directory listing directly. This avoids the platform-specific
	# wget dependency and the temporary file which used to be needed for it.
	try:
		response = requests.get(url0,timeout=(10,60))
		response.raise_for_status()
	except requests.RequestException:
		return [],[]

	lines = response.text.splitlines()
	n = np.size(lines)

	#now search for the line with the substring '.cdf"'
	urls = []
	fnames = []
	for i in range(0,n):
		if '.cdf"' in lines[i]:
			s = lines[i].replace('<a','"').replace('</a>','"').replace('>','"').split('"')
			for ss in s:
				if '.cdf' in ss and not 'http' in ss:
					urls.append(urljoin(url0,ss))
					fnames.append(ss)
					break
					
					
	return np.array(urls),np.array(fnames)
	
