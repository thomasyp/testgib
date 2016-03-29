#Differential Equation solver
import numpy as np

class Solver(object):
	def _init_(self):
		print "Created a Differential Equation solver!"
	
	def RKGContStepmethod(self,fuc,h,t,t_0,y_0):
		n = t/h
		t_p = t_0
		y_p = y_0
		a = (2**0.5-1)/2.0
		b = (2-2**0.5)/2.0
		c = -2**0.5/2.0
		d = 1+2**0.5/2.0
		for i in range(int(n)):
			k_1 = h*fuc(t_p,y_p)
		#	print "k_1:",k_1
			k_2 = h*fuc(t_p+h/2.0,y_p+k_1/2.0)
			k_3 = h*fuc(t_p+h/2.0,y_p+a*k_1+b*k_2)
			k_4 = h*fuc(t_p+h,y_p+c*k_3+d*k_3)
			y_n = y_p + (k_1+2*b*k_2+2*d*k_3+k_4)/6.0
			t_p = t_p + h
			y_p = y_n
	#	print "x_p:",t_p,"y_p:",y_p
		print y_n 
		return y_n
	
	def RKContStepmethod(self,fuc,h,t,t_0,y_0):
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
			print y_n
		return y_n
	
	def RKVarStepmethod(self,fuc,stepsize,t,t_0,y_0,eps):
		n = t/stepsize
		t_p = t_0
		tt = t_0
		y_p = y_0
		z_p = y_0
		for i in range(int(n)):
			k_1 = stepsize*fuc(t_p,y_p)
			k_2 = stepsize*fuc(t_p+stepsize/2.0,y_p+k_1/2.0)
			k_3 = stepsize*fuc(t_p+stepsize/2.0,y_p+k_2/2.0)
			k_4 = stepsize*fuc(t_p+stepsize,y_p+k_3)
			y_n = y_p + (k_1+2*k_2+2*k_3+k_4)/6.0
			t_p = t_p + stepsize
			y_p = y_n
			halftimesOfstepsize = 1
			max_yntozn = 1.0 + eps
			while(max_yntozn > eps):
				sub_stepsize = stepsize/(halftimesOfstepsize*2)
				for i in range(halftimesOfstepsize*2):
					kk_1 = sub_stepsize*fuc(tt,z_p)
					kk_2 = sub_stepsize*fuc(tt+sub_stepsize/2.0,z_p+kk_1/2.0)
					kk_3 = sub_stepsize*fuc(tt+sub_stepsize/2.0,z_p+kk_2/2.0)
					kk_4 = sub_stepsize*fuc(tt+sub_stepsize,z_p+kk_3)
					z_n = z_p + (kk_1+2*kk_2+2*kk_3+kk_4)/6.0
					tt = tt + sub_stepsize
					z_p = z_n
				yntozn_array = np.fabs(z_n - y_n)
				max_yntozn = yntozn_array.max()
				y_n = z_n
				halftimesOfstepsize = halftimesOfstepsize + 1				
			print z_n
		return z_n
		