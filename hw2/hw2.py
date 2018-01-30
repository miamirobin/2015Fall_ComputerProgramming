
from visual import *
import ruler
import math
g=9.8 # g = 9.8 m/s^2
v_initial=17.0 # for the initial velocity magnitude
theta_initial = math.radians(45)# for the initial angle that the projectile is launched over the ground
          # you can use sinusoidal functions to set up the initial velocity vector, such as
          # ball.v = v_initial * vector(cos(theta_initial), sin(theta_initial), 0)
drag_coef=0.3
drag_power =1.0

size = 0.25 # ball radius = 0.25 m
m =2.0
scene = display(title='bouncing projectile', center = (0,5,0),width=1200, height=800, background=(0.5,0.5,0))
floor = box(length=50, height=0.01, width=4, color=color.blue) # floor
ball = sphere(radius = size,color=color.red, make_trail=True) # ball
ruler1 = ruler.ruler(vector(-15, 0, 1), vector(1,0,0), unit = 2.0, length = 40.0, thickness = 0.2) # ruler1
ruler2 = ruler.ruler(vector(-15, 0, 1), vector(0,1,0), unit = 1.0, length = 10.0, thickness = 0.2) # ruler2
ball.pos = vector( -15.0, 0.0, 0.0) # ball initial position
ball.v = v_initial * vector(cos(theta_initial), sin(theta_initial), 0) 
dt = 0.001
magnitude = drag_coef *math.hypot(ball.v.x,ball.v.y) ** drag_power       # the drag force exerted on the projectile sets an acceleration with
                                                                          # magnitude = drag_ coef * v ** drag_power and the acceleration

c=0                                                                            # is anti-parallel to the velocity
while  c<3: # simulate until the ball touches the ground for the third time after launching
    rate(1000)
    ball.pos += ball.v*dt
    ball.v.x += magnitude/m*(-ball.v.x)/ math.hypot(ball.v.x,ball.v.y)*dt
    ball.v.y += - g*dt+magnitude/m*(-ball.v.y) / math.hypot(ball.v.x,ball.v.y)*dt
    if ball.y <= size and ball.v.y < 0: # check if ball hits the ground
        ball.v.y = - ball.v.y # if so, reverse y component of velocity
        c+=1
print ('distance = '),(ball.x+15) ,('m')
print 'end'
