import DiffEqSolver
import numpy as np

def testfuc(t,y):
	
	f1 = -0.08*y[0]**0.5-2*y[0]**0.2*y[1]
	f2 = -3.5e-6*y[0]**0.2*y[1]+1.6e-6*y[2]**0.3
	f3 = 2*y[0]**0.2*y[1]-0.16*y[2]**0.3
	f = np.array([f1,f2,f3])
#	print f
	return f
	
def testfuc2(t,y):
	
	f1 = -21.0*y[0]+19.0*y[1]-20.0*y[2]
	f2 = 19.0*y[0]-21.0*y[1]+20.0*y[2]
	f3 = 40.0*y[0]-40.0*y[1]-40.0*y[2]
	f = np.array([f1,f2,f3])
#	print f
	return f

def testfuc3(t,y):
	
	f1 = y[1]
	f2 = -y[0]
	f3 = -y[2]
	f = np.array([f1,f2,f3])
#	print f
	return f
	
sv = DiffEqSolver.Solver()
y0 = np.array([0.0,1.0,1.0])
sv.RKVarStepmethod(testfuc3,0.1,1,0,y0,0.000001)
#sv.RKContStepmethod(testfuc2,0.05,0.1,0,y0)
#testfuc(0,y)

#a = np.array([[1,2,3],[4,5,5]])
#b = np.array([2,1])

#a = np.array([[1,2,3],[4,5,5]])
#print a[0][0]
