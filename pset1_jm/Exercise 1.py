#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:58:07 2019

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
#####IntroCompPhys Exercise 1

###3

a=5.0
n0=0.0
n1=30.0
y0=100

def get_y_n(y_last, n1, n, a):
    if n<n1:
        y_n=1/(n+1)-a*y_last
        return get_y_n(y_n, n1, n+1, a)
    elif n>n1:
        y_n=(1/n-y_last)/a
        return get_y_n(y_n, n1, n-1, a)
    elif n==n1:
        return y_last

print(get_y_n(y0, n1, n0, a))

###4
G=1
M=1
h=0.01
steps=1000
class Body:
    def __init__(self, pos, vel, mass):
        self.pos=pos
        self.vel=vel
        self.startpos=pos
        self.startvel=vel
        self.mass=mass
        self.trail=[]
    def euler_step(self, h, other):
        vel=self.vel+h*G*(self.mass+other.mass)/np.linalg.norm(self.pos-other.pos)**3*(other.pos-self.pos)##calculate vi+1(xi,vi)
        pos=self.pos+h*self.vel##calculate xi+1(xi,vi)
        self.vel=vel
        self.pos=pos
        self.trail.append(self.pos)
    def leapfrog_position_step(self, h, other):
        self.pos=self.pos+h*self.vel##calculate xi+1(x(i),v(i+1/2) Step 1
        self.trail.append(self.pos)
    def leapfrog_velocity_step(self,h,other):
        self.vel=self.vel+h*G*(self.mass+other.mass)/np.linalg.norm(self.pos-other.pos)**3*(other.pos-self.pos)##calculate vi+3/2(vi+1/2,xi+1) Step 2
    def runge_lenz(self):
        """returns the runge lenz vector in case of an elliptical motion around r=0, otherwise useless"""
        return np.cross(self.mass*self.vel, np.array(np.cross(self.pos,self.mass*self.vel)))-self.mass*G*self.pos/np.linalg.norm(self.pos)##A=pX(rXp)-m*G*r/|r|
    def eccentricity(self):
        """returns the eccentricity vector in case of an elliptical motion around r=0, otherwise useless"""
        return self.runge_lenz()/(self.mass*G)
    def energy(self, other):
        """returns V(x1,x2)+1/2m*v**2 for 2 body problem"""
        return -G*self.mass*other.mass/np.linalg.norm(self.pos-other.pos)+0.5*self.mass*np.linalg.norm(self.vel)**2
    def reset(self):
        self.trail=[]
        self.vel=self.startvel
        self.pos=self.startpos
##euler
def euler(b1, b2, steps, h, plot_graph=True):
    i=0
    while i<steps:
        b1.euler_step(h, b2)
        b2.euler_step(h, b1)
        i+=1
    if plot_graph:
        plt.plot(np.array(b1.trail)[:,0], np.array(b1.trail)[:,1], label="Body 1")
        plt.plot(np.array(b2.trail)[:,0], np.array(b2.trail)[:,1], label="Body 2")
        plt.axis("equal")
        plt.title("Euler with h=%.5f, %i steps, b1_v0=(%.2f,%.2f)"%(h, steps, b1.startvel[0],b1.startvel[1]))
        plt.savefig("Euler with h=%.5f, %i steps, b1_v0=(%.2f,%.2f).png"%(h, steps, b1.startvel[0],b1.startvel[1]))
        plt.legend()
        plt.show()

b1=Body(np.array([0,0.5]),np.array([1,0]),M)
b2=Body(np.array([0,-0.5]),np.array([-1,0]),M)

##leapfrog
def leapfrog(b1, b2, steps, h, plot_graph=True):
    i=0
    while i<steps:
            b1.leapfrog_position_step(h, b2)
            b2.leapfrog_position_step(h, b1)
            b1.leapfrog_velocity_step(h, b2)
            b2.leapfrog_velocity_step(h, b1)
            i+=1
    if plot_graph:
        plt.axis("equal")
        plt.plot(np.array(b1.trail)[:,0], np.array(b1.trail)[:,1], label="Body 1")
        plt.plot(np.array(b2.trail)[:,0], np.array(b2.trail)[:,1], label="Body 2")
        plt.title("Leapfrog with h=%.5f, %i steps, b1_v0=(%.2f,%.2f)"%(h, steps, b1.startvel[0],b1.startvel[1]))
        plt.savefig("Leapfrog with h=%.5f, %i steps, b1_v0=(%.2f,%.2f).png"%(h, steps, b1.startvel[0],b1.startvel[1]))        
        plt.legend()
        plt.show()

b1=Body(np.array([0,0.5]),np.array([1,0]),M)
b2=Body(np.array([0,-0.5]),np.array([-1,0]),M)
##for this configuration (v=1) the bodys rotate in circular fashion, although euler integration has quite a high error with h=0.01 (see the plot),
##so leapfrog integration is already done here

euler(b1,b2,steps,h)
b1.reset()
b2.reset()
leapfrog(b1,b2,steps,h)

##now v=1/sqrt(2)

b1=Body(np.array([0,0.5,0]),np.array([1/np.sqrt(2),0,0]),M)
b2=Body(np.array([0,-0.5,0]),np.array([-1/np.sqrt(2),0,0]),M)
euler(b1,b2,steps,h)
b1.reset()
b2.reset()
leapfrog(b1,b2,steps,h)

##The bodies now rotate elliptic with a shared focus point
##eccentricity and runge lenz vector 
print("Eccentricity: (%.2f, %.2f), from Runge Lenz: (%.2f, %.2f)"%(b1.eccentricity()[0], b1.eccentricity()[1], b1.runge_lenz()[0],b1.runge_lenz()[1]))
##now v=1.5>sqrt(2)
b1=Body(np.array([0,0.5]),np.array([1.5,0]),M)
b2=Body(np.array([0,-0.5]),np.array([-1.5]),M)
euler(b1,b2,steps,h)
b1.reset()
b2.reset()
leapfrog(b1,b2,steps,h)
##the bodys fly away from each other

##now v0=0.3
b1=Body(np.array([0,0.5]),np.array([0.3,0]),M)
b2=Body(np.array([0,-0.5]),np.array([-0.3,0]),M)
euler(b1,b2,steps,h)
b1.reset()
b2.reset()
leapfrog(b1,b2,steps,h)
##The bodys "crash" into each other, leading to a high acceleration integration step catapulting them away from each other
##Can this be prevented by lowering the integration step time?

h=0.00001
steps=1000000##this may take a while
b1.reset()
b2.reset()
euler(b1,b2,steps,h)
b1.reset()
b2.reset()
leapfrog(b1,b2,steps,h)
##even euler kind of converges. WOW!


###5 Error Analysis

vs=[0.7,1.0,1.4]
hs=10**-np.linspace(2,5,7)

for v in vs:     
    b1=Body(np.array([0,0.5]),np.array([v,0]),M)
    b2=Body(np.array([0,-0.5]),np.array([-v,0]),M)
    errors=[]
    for h in hs:
        e_0=b1.energy(b2)
        euler(b1,b2,int(10/h),h, plot_graph=False)
        errors.append(np.abs(e_0-b1.energy(b2)))
        b1.reset()
        b2.reset()
    plt.plot(hs,errors)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("delta_t")
    plt.ylabel("Energy Error")
    plt.title("Energy Error caused by Euler step size with v0=%.1f"%v)
    plt.savefig("Energy Error caused by Euler step size with v0=%.1f.png"%v)
    plt.show()

###This is consistent with expectation since smaller steps=more exact (Taylor Series converges faster near x0)
###now leapfrog
for v in vs:     
    b1=Body(np.array([0,0.5]),np.array([v,0]),M)
    b2=Body(np.array([0,-0.5]),np.array([-v,0]),M)
    errors=[]
    for h in hs:
        e_0=b1.energy(b2)
        leapfrog(b1,b2,int(10/h),h, plot_graph=False)
        errors.append(np.abs(e_0-b1.energy(b2)))
        b1.reset()
        b2.reset()
    plt.plot(hs,errors)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("delta_t")
    plt.ylabel("Energy Error")
    plt.title("Energy Error caused by Leapfrog step size with v0=%.1f"%v)
    plt.savefig("Energy Error caused by Leapfrog step size with v0=%.1f.png"%v)
    plt.show()

##The Leapfrog Error, similar to Euler, grows with step size, but its two orders of magnitude smaller overall
##