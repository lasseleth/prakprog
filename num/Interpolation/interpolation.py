import math
import numpy as np


#def linterp(x:list, y:list):
#	assert len(x)==len(y)
#	def eval(z:float):
#		i=0; j=len(x)-1
#		while j-i>1 :
#			m=math.floor((i+j)/2)
#			if z>=x[m]: i=m
#			else      : j=m
#		return y[i]+(z-x[i])*(y[i+1]-y[i])/(x[i+1]-x[i])
#	return eval


def linterp(n:int, x:list, y:list, z:float):
#    assert(n>1 & z>=x[0] & z<=x[n-1])
    i=0
    j=n-1
    while(j-i>1):
        m=int(np.floor((i+j)/2))
        if(z>=x[m]): i=m
        else: j=m
        
    ai=y[i]
    bi=(y[i+1]-y[i])/(x[i+1]-x[i])
    return ai+bi*(z-x[i])


## Integration ##
def linterp_integ(n:int, x:list, y:list, z:float):
    
#	assert(n>1 & z>=x[0] & z<=x[n-1])
    
	i=0 
	j=n-1
	while(j-i>1):
		m=int(np.floor((i+j)/2))
		if(z>=x[m]): i=m
		else: j=m
	


	for k in range(i):
		ak = y[k]
		bk = (y[k+1]-y[k])/(x[k+1]-x[k])
		result = ak*(x[k+1]-x[k])+(bk/2)*(x[k+1]-x[k])*(x[k+1]-x[k])
    

	ai = y[i]
	bi = (y[i+1]-y[i])/(x[i+1]-x[i])
	result = ai*(z-x[i])+(bi/2)*(z-x[i])*(z-x[i])
	return result

#def linterp_integ(n:int, x:list, y:list, z:float):
#    
##	assert(n>1 & z>=x[0] & z<=x[n-1])
#    
#	i=0 
#	j=n-1
#	while(j-i>1):
#		m=int(np.floor((i+j)/2))
#		if(z>=x[m]): i=m
#		else: j=m
#	
#
#	result = np.zeros(0)
#
#	for k in range(i):
#		ak = y[k]
#		bk = (y[k+1]-y[k])/(x[k+1]-x[k])
#		result = np.append(result, ak*(x[k+1]-x[k])+(bk/2)*(x[k+1]-x[k])*(x[k+1]-x[k]))
#    
#
#		ai = y[i]
#		bi = (y[i+1]-y[i])/(x[i+1]-x[i])
#		result = np.append(result, ai*(z-x[i])+(bi/2)*(z-x[i])*(z-x[i]))
#	return result
#
#
