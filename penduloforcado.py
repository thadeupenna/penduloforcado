#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  penduloforcado.py
#  
#  Copyright 2017 Thadeu Penna <tjpp@dogfish>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt 

class Pendulo:
	def __init__(self,massa,l,v,theta):
		self.m = massa
		self.l = l 
		self.theta = theta
		self.v = v
		self.w2 = g/l 
		self.T = 2*math.pi*math.sqrt(l/g)
		
	def a(self,x,v):
		return -self.w2*math.sin(x) - gamma*v + A*math.sin(wf*tt)
			
	def move(self):
		at = self.a(self.theta,self.v)
		self.theta += self.v*dt + at*dt2/2
		atmp = self.a(self.theta,self.v)
		vtmp = self.v+(at+atmp)*dt/2 
		atmp = self.a(self.theta,vtmp)
		self.v += (atmp+at)*dt/2
		

dt = 5e-3
dt2 = dt*dt 
g = 9.8 
gamma = 0.5
A = 1.2

wf = 2./3.
m=1
p1 = Pendulo(1,10,0,math.pi/6)
tt=0
t=[0]
x=[p1.theta]
v=[p1.v]
while (tt<=45*p1.T):
	p1.move()
	tt+=dt 
	p1.theta=(p1.theta+math.pi)%(2*np.pi)-math.pi 
	x.append(p1.theta)
	v.append(p1.v)
	t.append(tt)
plt.figure(1)
relax=30000
xp = np.asarray(x[relax:])
vp = np.asarray(v[relax:])
tp = np.asarray(t[relax:])
plt.axis([-1,1,-1,1])
plt.axes().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('v')
plt.text(x[0]/max(x),v[0]/max(v),'S',color='red')
plt.scatter(xp/max(x),vp/max(v), s=0.0005)
plt.show()	
