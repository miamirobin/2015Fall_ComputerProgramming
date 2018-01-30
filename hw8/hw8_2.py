from visual import *
from visual.graph import*
import math
size, m = 0.02, 0.2
L, k = 0.2, 20.0
amplitude = 0.03
#scene1=gdisplay(y=400,width=1000,height=300,xtitle='t',ytitle='average power',background=(0.5,0.5,0))
#x=gdots(color=color.red,gdisplay=scene1)
scene = display(width=800, height=400, fov = 0.03, range = 0.8, center=(0.3, 0, 0), background=(0.5,0.5,0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue)# left wall
wall_right = box(length=0.005, height=0.3, width=0.3, color=color.blue)
ball = sphere(radius = size, color=color.red)# ball
ball2 = sphere(radius = size, color=color.red)
spring = helix(radius=0.015, thickness =0.01)#spring
spring1 = helix(radius=0.01, thickness =0.008)
spring2= helix(radius=0.015, thickness =0.01)
wall_left.pos = vector(0, 0, 0)
wall_right.pos = vector(0.6, 0, 0)
ball.pos, ball.v, ball.m = vector(L + amplitude, 0 , 0), vector(0, 0, 0), m
ball2.pos, ball2.v, ball2.m = vector(0.6-(L + amplitude), 0 , 0), vector(0, 0, 0), m
spring.pos = wall_left.pos
spring2.pos = wall_right.pos
spring1.pos=ball2.pos
b=0.05*(m*k)**0.5
t, dt = 0, 0.01
K=5
b1=0.05*(m*(k+K))**0.5
b2=0.025*(m*(k+K))**0.5
fa=0.1
wd=((k+K)/m)**0.5
F=fa*math.sin(wd*t)
average_power=F*ball.v
ball.pos=vector(L, 0, 0)
scene2=gdisplay(y=400,width=800,height=300, xtitle='Wd',ytitle='average_power',background=(0.4,0.4,0))
p=gcurve(color=color.cyan,gdisplay=scene2)
T=0
power=0
omega = [0.1*i + 0.7*sqrt((k+K)/m) for i in range(1, int(0.5*sqrt((k+K)/m)/0.1))]
for omega_d in omega:
    
    t, dt = 0, 0.02
    K=5
    b1=0.05*(m*(k+K))**0.5
    b2=0.025*(m*(k+K))**0.5
    fa=0.1
    wd=omega_d 
    F=fa*math.sin(wd*t)
    average_power=F*ball.v
    ball.pos=vector(L, 0, 0)
    ball2.pos, ball2.v, ball2.m = vector(0.6-(L + amplitude), 0 , 0), vector(0, 0, 0), m
    spring.pos = wall_left.pos
    spring2.pos = wall_right.pos
    spring1.pos=ball2.pos
    T=0
    power=0
    while T<2*math.pi/wd*31:
        rate(1000000)
        wd=omega_d
        F=fa*math.sin(wd*t)
        average_power=F*ball.v
        pp=mag(average_power)
        F1=vector(F, 0, 0)
        f1=-1*b1*ball.v
        f2=-1*b2*ball2.v
        spring1.pos=ball2.pos
        spring.axis = ball.pos-spring.pos# spring extended from spring endpoint A to ball
        spring2.axis = ball2.pos-spring2.pos
        spring1.axis=ball.pos-ball2.pos
        spring_force =-k * (mag(spring.axis)-L) * norm(spring.axis)# spring force vector
        spring_force2 =-k * (mag(spring2.axis)-L) * norm(spring2.axis)
    
        ball.a = (spring_force+f1+F1) / ball.m# ball acceleration = spring force /m
    
        ball.v +=ball.a*dt
        ball.pos += ball.v*dt
    
        ball2.a=(spring_force2+f2) / ball.m
        ball2.v+=ball2.a*dt
        ball2.pos+=ball2.v*dt
        T+=dt
        t += dt
        #x.plot(pos=(t,ball.pos.x-L))
        power+=pp*dt
        
        if T>=2*math.pi/wd*30:
            
            p.plot(pos=(wd, power/T))
               
        
