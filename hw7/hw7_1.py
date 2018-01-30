import math
I1=0.4*4/3*math.pi*(1250E3)**3*12.8E3*(1250E3)**2
I2=0.4*10.7E3*4/3*math.pi*(3500E3)**5-0.4*10.7E3*4/3*math.pi*(1250E3)**5
I3=0.4*4.5E3*4/3*math.pi*(6323E3)**5-0.4*4.5E3*4/3*math.pi*(3500E3)**5
I4=0.4*3.8E3*4/3*math.pi*(6357E3)**5-0.4*3.8E3*4/3*math.pi*(6323E3)**5
I=I1+I2+I3+I4
print 'inertia of Earth = ', I , ' kg*m^2'

w= 15*math.pi/180/60/60
L=I*w
print 'angular momentum of the Earth = ', L,' kg*m^2/s'
