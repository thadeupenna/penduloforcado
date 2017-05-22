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
			
dt = 1e-2
dt2 = dt*dt 
g = 9.8 
gamma = 0.5
A = 1.2
wf = 2./3.
m=1
p1 = Pendulo(1.,10.,0,math.pi/6)


tt=0
tmax=10*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0],v[0],e[0]=p1.theta,p1.v,p1.energy


for i in range(t.size):
	p1.move(t[i])
	x[i],v[i],e[i]=p1.theta,p1.v,p1.energy


relax=0



fig=plt.figure(2,figsize=(8,8),facecolor='white')
axes = plt.axes(xlim=(-math.pi,math.pi), ylim=(min(v),max(v)))
plt.xticks( [-3.14, -3.14/2,0, 3.14/2, 3.14],
        [r'$-\pi$', r'$-\pi/2$','0', r'$+\pi/2$', r'$+\pi$'])
plt.text(x[0],v[0],'S',color='red')
plt.xlabel('x')
plt.ylabel('v')
line, = axes.plot([], [], '.') 
timeleg = axes.text(0.02,0.9, '', transform=axes.transAxes)

def init():
	line.set_data([], [])
	timeleg.set_text('') 
	return line, timeleg
	
def animate(i):
	xa = x[:i]
	ya = v[:i]
	line.set_data(xa,ya)
	timeleg.set_text('t = %g' % t[i])
	return line, timeleg
	
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100000, interval=1e-6, blit=True)
                              
                              
fig=plt.figure(1,facecolor='lightgray')
fig.canvas.manager.window.wm_geometry('+100+400')
def graficoxt(pos,f,l,style,mostratics):
	plt.subplot(pos)
	axes = plt.gca()
	axes.axes.get_xaxis().set_visible(mostratics)
	axes.spines['top'].set_color('none')
	axes.spines['right'].set_color('none')
	axes.yaxis.set_ticks_position('left')
	axes.xaxis.set_ticks_position('bottom')
	axes.spines['bottom'].set_position(('data',0))
	plt.ylabel(l)
	plt.plot(t,f,style)

graficoxt(311,x,'x','r-',False)
graficoxt(312,v,'y','b-',False)
graficoxt(313,e,'E','g-',True)
                              
plt.show()
