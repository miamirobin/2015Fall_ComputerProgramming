from visual import *
import math
sizes = [0.05, 0.04]
ms = [0.2, 0.15]

b0size, b0m=sizes[0], ms[0]
b1size, b1m=sizes[1], ms[1]
g = 9.8 # g = 9.8 m/s^2
#size, m = 0.05, 0.2 # ball size = 0.05 m, ball mass = 0.2kg
r, k = 0.5, 10 # spring original length = 0.5m, force constant = 10 N/m
scene = display(width=800, height=800, center=(0, -0.2, 0), background=(0.5,0.5,0)) # open window
#ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue) # ceiling
b0 = sphere(radius = b0size, color=color.red) # ball
b1 = sphere(radius = b1size, color=color.yellow)
spring = helix(pos=b0.pos,radius=0.02, thickness =0.01) # spring endpoint A at (0,0,0), 10 coils
b0.pos = vector(0, 0 , 0) # ball initial position
b1.pos = vector(-r-0.2, 0, 0)
b0.v = vector(0.1, 0, 0)
b1.v = vector(-0.1, 0, 0) # ball initial velocity
T=0
dt = 0.001
while True:
    
    rate(1000)
    spring.axis =  b1.pos-b0.pos
    spring.pos=b0.pos
      # spring extended from spring endpoint A to ball
    spring_force = - k * (mag(spring.axis) - r) * spring.axis / mag(spring.axis) # spring force vector
    b0.a =  -spring_force / b0m # ball acceleration = - g in y + spring force /m
    b0.v += b0.a*dt
    b0.pos += b0.v*dt
    b1.a =  spring_force / b1m # ball acceleration = - g in y + spring force /m
    b1.v += b1.a*dt
    b1.pos += b1.v*dt
    T+=dt
    if T>=2*math.pi*((b0m+b1m)/2/k)**0.5:
        print ' the averaged center of mass = '+str((b0m*b0.pos+b1m*b1.pos)/(b0m+b1m))
        print ' the period = '+str(T)+' second'
        print ' '
        T=0
