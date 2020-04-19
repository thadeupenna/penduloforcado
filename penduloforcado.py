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
A = 1.1
wf = 2./3.
m=1
p1 = Pendulo(1.,10.,0,-np.pi/6)


tt=0
tmax=15*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0],v[0],e[0]=p1.theta,p1.v,p1.energy

for i in range(t.size):
	p1.move(t[i])
	x[i],v[i],e[i]=p1.theta,p1.v,p1.energy

#print(plt.style.available)
plt.style.use('fivethirtyeight')
#plt.style.use('seaborn-paper')

fig=plt.figure(figsize=(18,8),facecolor='white')

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')
thetaxt = fig.add_subplot(331,ylim=(-math.pi,math.pi))
ax = plt.gca()
#plt.yticks( [-3.14, -3.14/2,0, 3.14/2, 3.14],
#        [r'$-\pi$', r'$-\pi/2$','0', r'$\pi/2$', r'$\pi$'])
ax.xaxis.grid(True)
ax.yaxis.grid(True)
plt.setp(thetaxt.get_xticklabels(), visible = False) 
line2, = thetaxt.plot([], [], 'ro', markersize=2)

vxt = fig.add_subplot(334,ylim=(min(v),max(v)), sharex = thetaxt)
ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(True)
plt.setp(vxt.get_xticklabels(), visible = False) 
line3, = vxt.plot([], [], 'g-')

ext = fig.add_subplot(337,ylim=(min(e),max(e)), sharex=thetaxt)
ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(True)
plt.rc('text', usetex=False)
plt.setp(ext.get_xticklabels(), visible = True) 
line4, = ext.plot([], [], 'b-')

l=p1.l
xp=np.sin(x)*l
yp=-np.cos(x)*l
pendulo = fig.add_subplot(132,xlim=(-l*1.1,l*1.1),ylim=(-l*1.1,l*1.1),aspect='equal')
plt.axis('off')
line5 = [] 
lob = pendulo.plot([], [], 'r-')[0]
line5.append(lob)
lob = pendulo.plot([], [], 'ko-',markersize=8)[0]
line5.append(lob)
# print len(line5)
	
phase = fig.add_subplot(133,xlim=(-math.pi,math.pi), ylim=(min(v),max(v)))
#plt.xticks( [-3.14, -3.14/2,0, 3.14/2, 3.14],
#        [r'$-\pi$', r'$-\pi/2$','0', r'$+\pi/2$', r'$+\pi$'])
#plt.text(x[0],v[0],'S',color='red')
phase.xaxis.set_ticks_position('top')
plt.xlabel('x')
plt.ylabel('v')
line, = phase.plot([], [], 'ko', markersize=2) 
timeleg = phase.text(0.02,0.9, '', transform=phase.transAxes)
plt.subplots_adjust( hspace = 0.1)


def init():
	line.set_data([], [])
	line2.set_data([], [])
	line3.set_data([], [])
	line4.set_data([], [])
	for lined in line5:
		lined.set_data([], [])
	timeleg.set_text('') 
	return line, line2, line3, line4, line5, timeleg
	
def animate(i):
	xa = x[:i]
	ya = v[:i]
	imin = 0 if  i < 10 else i-10
	pendx = xp[imin:i+1]
	pendy = yp[imin:i+1]
	massx = [0 , xp[i]]
	massy = [0 , yp[i]]
	line.set_data(xa,ya)
	thetaxt.set_xlim(0,t[i])
	ext.set_xlim(0,t[i])
	line2.set_data(t[:i],x[:i])
	line3.set_data(t[:i],v[:i])
	line4.set_data(t[:i],e[:i])
	line5[0].set_data(pendx,pendy)
	line5[1].set_data(massx,massy)
	timeleg.set_text('t = %g' % t[i])

	return line, line2, line3, line4, line5, timeleg
	
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=t.size, interval=1, blit=False,repeat=False)
#anim.save('basic_animation.mp4', fps=120, extra_args=['-vcodec', 'libx264'])                          

plt.show()
