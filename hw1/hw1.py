from visual import *
g=9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
height = 2.0 # ball center initial height = 15 m
scene = display(width=800, height=800, center = (0,height/2,0), background=(0.5,0.5,0)) # open a window
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius = size, color=color.red) # the ball
ball.pos = vector( -15, height, 0) # ball center initial position
ball.v = vector(8, 8 , 0) # ball initial velocity
a1 = arrow(shaftwidth=0.1)
a1.pos = vector(-14.5,2.5,0)
t=0
a1.color = color.yellow
dt = 0.001 # time step
while ball.pos.y >= size: # until the ball hit the ground
 rate(1000) # run 1000 times per real second

 ball.pos += ball.v*dt
 ball.v.y += - g*dt
 a1.axis = ball.v *0.1
 a1.pos +=ball.v*dt
 t += dt 

print ('t='),(t),('second') 
print 'end'
