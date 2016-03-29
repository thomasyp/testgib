#Euler method
import numpy as np

def Eulermethod(fuc,h,l,x_0,y_0):
	n = l/h
	x_p = x_0
	y_p = y_0
	for i in range(int(n)):
		y_n_ = y_p + h * fuc(x_p,y_p)
		x_n = x_p + h
		y_n = y_p + h / 2.0 * (fuc(x_p,y_p)+fuc(x_n,y_n_)) 
		y_p = y_n
		x_p = x_n
		#print "x_p:",x_p,"y_p:",y_p
	print y_n

def RKmethod(fuc,h,l,x_0,y_0):
	n = l/h
	x_p = x_0
	y_p = y_0
	for i in range(int(n)):
		k_1 = h*fuc(x_p,y_p)
		k_2 = h*fuc(x_p+h/2.0,y_p+k_1/2.0)
		k_3 = h*fuc(x_p+h/2.0,y_p+k_2/2.0)
		k_4 = h*fuc(x_p+h,y_p+k_3)
		y_n = y_p + (k_1+2*k_2+2*k_3+k_4)/6.0
		x_p = x_p + h
		y_p = y_n
		#print "x_p:",x_p,"y_p:",y_p
	print y_n
	
def RKGmethod(fuc,h,l,x_0,y_0):
	n = l/h
	x_p = x_0
	y_p = y_0
	a = (2**0.5-1)/2.0
	b = (2-2**0.5)/2.0
	c = -2**0.5/2.0
	d = 1+2**0.5/2.0
	for i in range(int(n)):
		k_1 = h*fuc(x_p,y_p)
		k_2 = h*fuc(x_p+h/2.0,y_p+k_1/2.0)
		k_3 = h*fuc(x_p+h/2.0,y_p+a*k_1+b*k_2)
		k_4 = h*fuc(x_p+h,y_p+c*k_3+d*k_3)
		y_n = y_p + (k_1+2*b*k_2+2*d*k_3+k_4)/6.0
		x_p = x_p + h
		y_p = y_n
		#print "x_p:",x_p,"y_p:",y_p
	print y_n

def testfuc(x,y):
	return 100*(1-np.exp(-x)-y)
	
Eulermethod(testfuc,0.0001,0.1,0,0)
RKmethod(testfuc,0.0001,0.1,0,0)
