from visual import *
import math
g = 9.8  # m/s^2
M, R, w = 0.5, 0.10, 0.05 # mass, radius, thickness of the central part   
I = 0.5 * M * R ** 2 # rotational inertia of the spinning top
l, r = 0.16, 0.005  # length, radius of the MASSLESS shaft
theta =  70* math.pi / 180.0 # initial upright angle relative to the horizon  
Omega = 10*2*math.pi * vector(cos(theta), sin(theta), 0) # initial angular velocity
theta1 = 30* math.pi / 180.0
omega2= 10*2*math.pi * vector(0, cos(theta1), sin(theta1))
lr = 0.08  # the distance from the bottom to the center of mass of the spinning top
scene = display(width = 1000, height = 1000, range = 0.6, background = (0.5, 0.5, 0))
spintop = frame()
k=0.5*math.pi
shaft = cylinder(frame=spintop, pos=(0,0,0), axis =(1,math.cos(k),math.sin(k)), radius=r, length=l,material = materials.wood)
disk = cylinder(frame=spintop, pos=(lr-w/2,0,0), axis = (w,w*math.cos(k),w*math.sin(k)), radius=R, material = materials.wood)
spintop.pos = (0,0,0)
base = cone(pos=(0,-0.2,0), axis=(0,0.2,0), color = color.blue, radius=0.1)
dt = 0.0002

while True:
    rate(1000)
    
    spintop.axis = Omega
    delta_angle = mag(Omega) * dt
    k+=0.01*math.pi
    theta1+=mag(omega2)*dt
    
    
    spintop.rotate(angle=delta_angle)
    
    Omega = 10*2*math.pi * vector(cos(theta), sin(theta), 0) 
