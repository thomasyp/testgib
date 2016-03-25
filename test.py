#Euler method
import numpy as np

def Eulermethod(fuc,h,l,x_0,y_0):
	n = l/h
	x_p = x_0
	y_p = y_0
	for i in range(int(n)):
		y_n = y_p + h * fuc(x_p,y_p)
		x_p = x_p + h 
		y_p = y_n
		print "x_p:",x_p,"y_p:",y_p
		print y_n
	

def testfuc(x,y):
	return x*x*y
	
Eulermethod(testfuc,0.1,0.5,0,1)
