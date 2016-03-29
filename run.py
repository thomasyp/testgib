import DiffEqSolver
import numpy as np

def testfuc(t,y):
	
	f1 = -0.08*y[0]**0.5-2*y[0]**0.2*y[1]
	f2 = -3.5e-6*y[0]**0.2*y[1]+1.6e-6*y[2]**0.3
	f3 = 2*y[0]**0.2*y[1]-0.16*y[2]**0.3
	f = np.array([f1,f2,f3])
#	print f
	return f


sv = DiffEqSolver.Solver()
y = np.array([0.95,0.05,0])
sv.RKGmethod(testfuc,0.01,7.0,0,y)
#testfuc(0,y)

#a = np.array([[1,2,3],[4,5,5]])
#b = np.array([2,1])

#a = np.array([[1,2,3],[4,5,5]])
#print a[0][0]
