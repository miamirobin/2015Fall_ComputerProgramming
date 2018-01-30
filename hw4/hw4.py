from visual import *
import math
g=9.8               #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
L = 1.0             #細線長 1.0m
theta = 45*math.pi/180 #單擺起始角度 = 30 degrees
phi=0
omega = 0           #初角速度 = 0

scene = display(width=1200, height=1000,center = (0, -L/2, 0), background=(0.5,0.5,0))     #設定畫面
ceiling = box(length=2, height=0.001, width=2, color=color.blue)    #畫天花板
string0 = cylinder(pos=(0, 0, 0), radius=0.03)
ball = sphere(radius = size,  color=color.red)                      #畫球
string = cylinder(pos=(0, 0, 0), radius=0.003)                      #畫細線，一端在(0,0,0)
w=2*math.pi/2.087      
ball.v = vector (0, 0, w*L*math.sin(theta))
string0.axis = vector (0, -1.5, 0)

ball.pos = vector(L *math.cos(phi)* math.sin(theta), -L*math.cos(theta), L *math.sin(phi)* math.sin(theta) )
dt = 0.001
T=0
while True:
    rate(1000)

    alpha = -g*math.sin(theta)/L
    omega += alpha*dt
    theta += omega*dt
    
    T+=dt
    phi +=w*dt
    #T=2*math.pi*
    ball.pos = vector(L *math.sin(phi)* math.sin(theta), -L*math.cos(theta), L*math.cos(phi)* math.sin(theta) )
    
    string.axis = ball.pos - string.pos
    #if T==2*math.pi/w:
    if theta >= 45*math.pi/180:
        print 'T= ',(T),' second'
        T=0
    
