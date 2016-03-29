#Differential Equation solver
import numpy as np

class Solver(object):
	def _init_(self):
		print "Created a Differential Equation solver!"
	
	def RKGmethod(self,fuc,h,t,t_0,y_0):
		n = t/h
		t_p = t_0
		y_p = y_0
		a = (2**0.5-1)/2.0
		b = (2-2**0.5)/2.0
		c = -2**0.5/2.0
		d = 1+2**0.5/2.0
		for i in range(int(n)):
			k_1 = h*fuc(t_p,y_p)
			print "k_1:",k_1
			k_2 = h*fuc(t_p+h/2.0,y_p+k_1/2.0)
			k_3 = h*fuc(t_p+h/2.0,y_p+a*k_1+b*k_2)
			k_4 = h*fuc(t_p+h,y_p+c*k_3+d*k_3)
			y_n = y_p + (k_1+2*b*k_2+2*d*k_3+k_4)/6.0
			t_p = t_p + h
			y_p = y_n
		print "x_p:",t_p,"y_p:",y_p
		print y_n 
		return y_n
	def RKmethod(self,fuc,h,t,t_0,y_0):
		n = t/h
		t_p = t_0
		y_p = y_0
		for i in range(int(n)):
			k_1 = h*fuc(t_p,y_p)
		#	print k_1
		#	print y_p+k_1/2.0
			k_2 = h*fuc(t_p+h/2.0,y_p+k_1/2.0)
			k_3 = h*fuc(t_p+h/2.0,y_p+k_2/2.0)
			k_4 = h*fuc(t_p+h,y_p+k_3)
			y_n = y_p + (k_1+2*k_2+2*k_3+k_4)/6.0
			t_p = t_p + h
			y_p = y_n
		#	print "t_p:",t_p,"y_p:",y_p,'k1:',k_1,"k2:",k_2,k_1,"k2:",k_3,"k4:",k_4
		print y_n
		return y_n
