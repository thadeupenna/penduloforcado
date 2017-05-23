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
			
dt = 5e-2
dt2 = dt*dt 
g = 9.8 
gamma = 0.5
A = 3
wf = 2./3.
m=1
p1 = Pendulo(1.,10.,0,-np.pi/2)


tt=0
tmax=100*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0],v[0],e[0]=p1.theta,p1.v,p1.energy

for i in range(t.size):
	p1.move(t[i])
	x[i],v[i],e[i]=p1.theta,p1.v,p1.energy


fig=plt.figure(figsize=(18,8),facecolor='white')


thetaxt = fig.add_subplot(331,xlim=(0,max(t)),ylim=(-math.pi,math.pi))
ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(False)
plt.setp(thetaxt.get_xticklabels(), visible = False) 
line2, = thetaxt.plot([], [], 'r.', markersize=0.5)

vxt = fig.add_subplot(334,xlim=(0,max(t)),ylim=(min(v),max(v)),sharex = thetaxt)
ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(False)
plt.setp(vxt.get_xticklabels(), visible = False) 
line3, = vxt.plot([], [], 'g-')

ext = fig.add_subplot(337,xlim=(0,max(t)),ylim=(min(e),max(e)))
ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(False)
line4, = ext.plot([], [], 'b-')

l=p1.l
xp=np.sin(x)*l
yp=-np.cos(x)*l
pendulo = fig.add_subplot(132,xlim=(-l,l),ylim=(-l,l),aspect='equal')
plt.axis('off')
line5, = pendulo.plot([], [], 'ro-',markersize=4)


phase = fig.add_subplot(133,xlim=(-math.pi,math.pi), ylim=(min(v),max(v)),aspect='equal')
plt.xticks( [-3.14, -3.14/2,0, 3.14/2, 3.14],
        [r'$-\pi$', r'$-\pi/2$','0', r'$+\pi/2$', r'$+\pi$'])
plt.text(x[0],v[0],'S',color='red')
phase.xaxis.set_ticks_position('top')
plt.xlabel('x')
plt.ylabel('v')
line, = phase.plot([], [], '.', markersize=2) 
timeleg = phase.text(0.02,0.9, '', transform=phase.transAxes)
plt.subplots_adjust( hspace = 0)


def init():
	line.set_data([], [])
	line2.set_data([], [])
	line3.set_data([], [])
	line4.set_data([], [])
	line5.set_data([], [])
	timeleg.set_text('') 
	return line, line2, line3, line4, line5, timeleg
	
def animate(i):
	xa = x[:i]
	ya = v[:i]
	pendx = [0, xp[i] ]
	pendy = [0, yp[i] ]
	line.set_data(xa,ya)
	line2.set_data(t[:i],x[:i])
	line3.set_data(t[:i],v[:i])
	line4.set_data(t[:i],e[:i])
	line5.set_data(pendx,pendy)
	timeleg.set_text('t = %g' % t[i])

	return line, line2, line3, line4, line5, timeleg
	
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=t.size-4, interval=0.001, blit=True)
plt.show()
