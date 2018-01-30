# modified from https://www.youtube.com/watch?v=fyzblLPzktA&t=473s   AP Physics project by Chris C. and Jeremy Z.


#Author: yochi


from __future__ import division
from visual import *
from visual.graph import *

#Functions

def pol2cart(theta):
    #
    return vector(cos(1.5*pi+theta ) * L, sin((1.5*pi+theta)) * L, 0)

def pol2cart2(theta):
    return vector(sin((theta))*2/3, 0, cos((theta))*2/3)

def latang(phi):
    return 2 * pi * sin(phi) /time #86164.0905

#Constants

g = vector(0,9.8,0)
L = 1
lat = 25*pi/180 #Latitude
time = 86400/85.1735 #length of day in seconds 86164.0905 on earth

#Objects
scene = display(x=800,title='focault pendulum', width=500, height=700, background=(0.5,0.5,0))
pegs = frame(pos = vector(0,-1.1,0))
#?width

ceiling = box(frame=pegs,pos=vector(0,0.0,0)-pegs.pos,length=0.5,height=0.05,width=1)
ball=sphere(pos=vector(0,0,0),radius=0.1,color=color.yellow)
floor=cylinder(pos=vector(0,-1.1,0),radius=0.6,length=0.07, width=1,axis=vector(0,0.1,0),color=color.green)
string=curve(pos=[vector(0,0,0),ball.pos], radius = 0.01)
trail = curve(frame=pegs)

alpha = 0
for d in range(0,360,15):
        cylinder(frame=pegs,axis=(0,0.15,0),radius=0.03,color=color.cyan,pos=(0.6*cos(d/180*math.pi),0,0.6*sin(d/180*math.pi) ))
while alpha < 2*pi:
    #?pos
    
    alpha = alpha + pi/6

graphtheta = gdisplay(height=700)
massmovement = gcurve(color=color.red,gdisplay=graphtheta)
for i in arange(0.,5,0.01):
    massmovement.plot

#Scene
scene.frame = pegs
#Scene.stereo = 'redcyan'
scene.userspin = False

#Values

#Ball 1
L = 1
theta = pi / 8 #Initial theta

ball.pos = pol2cart(theta)
ball.m = 5
ball.L = vector(0,0,0)
ball.I = ball.m * mag(ball.pos) ** 2

string.pos = [vector(0,0,0), ball.pos]

#Omega = (mag(g)/L) ** (1/2)
Fg = -ball.m * g
Tg = cross(ball.pos,Fg)

#Independent Variables

beta = 0
t = 0
dt = 0.01

#Loop

while True :
    False
    rate(100)

    Tg = cross(ball.pos,Fg)
    
    ball.L = ball.L + Tg*dt
    theta = theta + ball.L.z / ball.I * dt

    ball.pos = pol2cart(theta)
    string.pos = [vector(0,0,0),ball.pos]

    if t < 24:#?ball.pos.z
        trail.append(pos=vector(ball.pos.x*cos(beta),ball.pos.y-pegs.pos.y,ball.pos.x*sin(beta)))

    pegs.rotate(angle=(latang(lat)), axis=vector(0,1,0), origin=pegs.pos)

    beta = beta + latang(lat)
    scene.forward = -pol2cart2(beta)

    if t < 24:
        massmovement.plot(pos=(ball.pos.x*sin(beta),ball.pos.x*cos(beta)))

    t = t + dt
