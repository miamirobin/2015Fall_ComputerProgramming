from visual import *
import math


r = 0.3 #spring original length
k = 25.0 #spring constant
size = [0.05, 0.04, 0.03] #ball radius
ms = [0.5, 0.4, 0.3] #ball mass
colors = [color.yellow, color.green, color.blue] #ball color
position = [vector(0, 0, 0), vector(0, -r, 0), vector(0.25,-0.45, 0)] #ball initial position
velocity = [vector(0, 0, 0), vector(0, 0, 0), vector(-0.2, 0.42, 0)] #ball initial velocity
b0size, b0m=size[0], ms[0]
b1size, b1m=size[1], ms[1]
b2size, b2m=size[2], ms[2]

g = 9.8 # g = 9.8 m/s^2
#size, m = 0.05, 0.2 # ball size = 0.05 m, ball mass = 0.2kg
# spring original length = 0.5m, force constant = 10 N/m
scene = display(width=800, height=800, center=(-0.8, 0.4, 0), background=(0.5,0.5,0)) # open window
#ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue) # ceiling
b0 = sphere(radius = b0size, color=color.red) # ball
b1 = sphere(radius = b1size, color=color.yellow)
b2 = sphere(radius = b2size, color=color.blue)
b3 = sphere(radius = 0.1*b2size, color=color.green)

spring = helix(pos=b0.pos,radius=0.02, thickness =0.01) # spring endpoint A at (0,0,0), 10 coils
b0.pos = vector(0, 0, 0) # ball initial position
b1.pos = vector(0, -r, 0)
b2.pos = vector(0.25,-0.45, 0)
b3.pos = b0.pos
b0.v = vector(0, 0, 0)
b1.v = vector(0, 0, 0) # ball initial velocity
b2.v = vector(-0.2, 0.42, 0)
vc= (b0.v*b0m+b1.v*b1m+b2.v*b2m) / (b0m+b1m+b2m)
vvc =(b0.v*b0m+b2.v*b2m) / (b0m+b2m)
T=0
dt = 0.001
z=0.5*b2m*(mag(b2.v))**2
c=b2m*(b2.v)
power=0
ek=0
pp=0

print 'kinetic energy of balls[2] and its momentum= ',z,' J and ',c,' kg*m/s'
print ''
while True:
    b2.pos +=b2.v*dt
    
    if mag(b0.pos-b2.pos)<=b0size+b2size:
        b0.v=2*vvc-b0.v
        b2.v=2*vvc-b2.v
        
    
    rate(1000)
    spring.axis =  b1.pos-b0.pos
    spring.pos=b0.pos               # spring extended from spring endpoint A to ball
    
    spring_force = - k * (mag(spring.axis) - r) * spring.axis / mag(spring.axis) # spring force vector
    b0.a =  -spring_force / b0m # ball acceleration = - g in y + spring force /m
    b0.v += b0.a*dt
    b0.pos += b0.v*dt
    b1.a =  spring_force / b1m # ball acceleration = - g in y + spring force /m
    b1.v += b1.a*dt
    b1.pos += b1.v*dt
    b3.pos=b1.pos
    power+= 0.5*k*(mag(spring.axis) - r)**2*dt
    b0v=mag(b0.v)
    b1v=mag(b1.v)
    vcc= mag(b1m*b1.v+b0m*b0.v)/(b1m+b0m)
    
    pp=(b0m*b0.v+b1m*b1.v)
    ek+=(0.5*b1m*(mag(b1.v))**2+ 0.5*b0m*(mag(b0.v))**2)*dt
    T+=dt
    if T>=2*math.pi*((b0m+b1m)/2/k)**0.5:
        print ' Internal Vibrational Potential Energy averaged over a period = ',power/T ,' J'
        
        print ' Internal Vibrational Kinetic Energy averaged over a period = ',0.67*ek/T,' J'
        print ' Internal Rotational Kinetic Energy averaged over a period = ',0.33*ek/T,' J'
        print ' Center of Mass Kinetic Energy = ',0.5*(b0m+b1m)* (vcc**2),' J'
        print ' Kinetic Energy of ball2= ',0.5*b2m*(mag(b2.v))**2,' J'
        print ' Total Energy = ' , power/T + ek/T +0.5*(b0m+b1m)* (vcc**2)+ 0.5*b2m*(mag(b2.v))**2, ' J'
        print ' Linear Momentum of the spring-ball system = ', pp ,' kg*m/s'
        print ' Linear Momentum of ball [2] = ',(b2m*b2.v), ' kg*m/s'
        print ' Total Linear Momentum = ',(pp+b2m*b2.v), 'kg*m/s'
        print ' '
        
       
        
        
        power=0
        ek=0
        T=0
