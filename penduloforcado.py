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
import matplotlib.animation as animation

class Pendulo:
	def __init__(self,massa,l,v,theta):
		self.m = massa
		self.l = l 
		self.theta = theta
		self.v = v
		self.w2 = g/l 
		self.T = 2*math.pi*math.sqrt(l/g)
		self.k = massa*self.w2
		self.energy = 0.5*massa*(l*v)**2+m*g*l*(1-math.cos(theta))
		
	def a(self,x,v,tt):
		return -self.w2*math.sin(x) - gamma*v + A*math.sin(wf*tt)
				
	def move(self,tt):
		at = self.a(self.theta,self.v,tt)
		self.theta += self.v*dt + at*dt2/2
		atmp = self.a(self.theta,self.v,tt)
		vtmp = self.v+(at+atmp)*dt/2 
		atmp = self.a(self.theta,vtmp,tt)
		self.v += (atmp+at)*dt/2
		p1.theta=(p1.theta+math.pi)%(2*math.pi)-math.pi 
		self.energy = 0.5*self.m*(self.l*self.v)**2 + (
		 self.m*g*self.l*(1-math.cos(self.theta)))
			
dt = 2e-2
dt2 = dt*dt 
g = 9.8 
gamma = 0.5
A = 1.2
wf = 2./3.
m=1
p1 = Pendulo(1.,10.,0,math.pi/6)


tt=0
tmax=20*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0],v[0],e[0]=p1.theta,p1.v,p1.energy

for i in range(t.size):
	p1.move(t[i])
	x[i],v[i],e[i]=p1.theta,p1.v,p1.energy


fig=plt.figure(figsize=(8,8),facecolor='white')

phase = fig.add_subplot(211,xlim=(-math.pi,math.pi), ylim=(min(v),max(v)))
plt.xticks( [-3.14, -3.14/2,0, 3.14/2, 3.14],
        [r'$-\pi$', r'$-\pi/2$','0', r'$+\pi/2$', r'$+\pi$'])
plt.text(x[0],v[0],'S',color='red')
plt.xlabel('x')
plt.ylabel('v')
line, = phase.plot([], [], '.', markersize=0.6) 
timeleg = phase.text(0.02,0.9, '', transform=phase.transAxes)

thetaxt = fig.add_subplot(614,xlim=(0,max(t)),ylim=(-math.pi,math.pi))
line2, = thetaxt.plot([], [], 'r.', markersize=0.2)

vxt = fig.add_subplot(615,xlim=(0,max(t)),ylim=(min(v),max(v)))
line3, = vxt.plot([], [], 'g-')

ext = fig.add_subplot(616,xlim=(0,max(t)),ylim=(min(e),max(e)))
line4, = ext.plot([], [], 'b-')

def init():
	line.set_data([], [])
	line2.set_data([], [])
	line3.set_data([], [])
	line4.set_data([], [])
	timeleg.set_text('') 
	return line, line2, line3, line4, timeleg
	
def animate(i):
	xa = x[:i]
	ya = v[:i]
	line.set_data(xa,ya)
	line2.set_data(t[:i],x[:i])
	line3.set_data(t[:i],v[:i])
	line4.set_data(t[:i],e[:i])
	timeleg.set_text('t = %g' % t[i])
	return line, line2, line3, line4, timeleg
	
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100000, interval=1e-6, blit=True)
                    
plt.show()
