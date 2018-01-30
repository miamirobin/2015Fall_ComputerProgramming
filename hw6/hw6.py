import math
from visual import *

# Data in units according to the International System of Units
G = 6.67 * math.pow(10,-11)

# Mass of the Earth
ME = 5.974 * math.pow(10,24)
# Mass of the Mars
MM = 6.418 * math.pow(10,23)
# Mass of the Sun
MS = 1.989 * math.pow(10,30)
MH = 2.2 * math.pow(10,14)
# Radius Earth-Moon
REM = 384400000
# Radius Sun-Earth
RSE = 147100000000
# Radius Sun-Mars
RSM = 206600000000
RSH = 87.66E9
# Force Earth-Moon
FEM = G*(ME*MM)/math.pow(REM,2)
# Force Earth-Sun
FES = G*(MS*ME)/math.pow(RSE,2)
# Force Mars-Sun
FMS = G*(MS*MM)/math.pow(RSM,2)
FSH = G*(MS*MH)/math.pow(RSH,2)

# Angular velocity of the Mars with respect to the Sun (rad/s)
wM = math.sqrt(FMS/(MM * RSM))
# Velocity v of the Mars (m/s)
vM = wM*RSM
wH = wM/76
# Velocity v of the Mars (m/s)
#vH = wH*RSH


# Angular velocity of the Earth with respect to the Sun(rad/s)
wE = math.sqrt(FES/(ME * RSE))
# Velocity v of the Earth (m/s)
vE = wE*RSE

# Initial angular position
theta0 = 0

# Position at each time
def positionMars(t):
    theta = theta0 + wM * t
    return theta

def positionEarth(t):
    theta = theta0 + wE * t
    return theta
def positionHalley(t):
    theta = math.pi + wH * t
    return theta


def fromDaysToS(d):
    s = d*24*60*60
    return s

def fromStoDays(s):
    d = s/60/60/24
    return d

def fromDaysToh(d):
    h = d * 24
    return h


days = 365
seconds = fromDaysToS(days)
scene = display(width=10000, height=10000, center=(40, 0, 0), background=(0.5,0.5,0)) # open window
print ('theoretical period for Earth=: '),seconds,' s'
print ('theoretical period for Mars =: '),1.88*seconds,' s'
print ' '
colors = [color.yellow, color.green, color.blue, color.orange]
material=[materials.earth]
v = vector(0.5,0,0)
E = sphere(pos=vector(4.2,0,0),color=color.cyan,material=materials.earth,radius=0.35,make_trail=True)
S = sphere(pos=vector(0,0,0),color=color.orange,radius=1)
M= sphere(pos=vector(5.045,0,0),color=color.red,radius=0.22,make_trail=True)
H= sphere(pos=vector(-1.83,0,0),color=color.green,radius=0.15,make_trail=True)
T = 0
t=0
n=0
thetaTerra1 = 0
dt = 86400
a=54
b=13.77
c=52.17
dthetaE = positionEarth(t+dt)- positionEarth(t)
dthetaM = positionMars(t+dt) - positionMars(t)
dthetaH = positionHalley(t+dt) - positionHalley(t)
l=1.83 * 54.55E3
R=math.hypot(a*math.cos(positionHalley(n))+c,b*math.sin(positionHalley(n)))
vH=l/R
def potential(n):
    R=math.hypot(a*math.cos(positionHalley(n))+c,b*math.sin(positionHalley(n)))
    return -1*G*MS*MH/(R*47.9E9)
def ek(n):
    R=math.hypot(a*math.cos(positionHalley(n))+c,b*math.sin(positionHalley(n)))

    vH=l/R
    return 0.5*MH*abs(vH)**2


a=54
b=13.77
c=52.17
theta=0
q=0
w=0
z=0
x=0
k=0
while True:
    rate(500)
    thetaEarth = positionEarth(t+dt)- positionEarth(t)
    thetaMars = positionMars(t+dt) - positionMars(t)
    thetaHalley = positionHalley(t+dt) - positionHalley(t)
    
    # Rotation only around z axis (0,0,1)
    E.pos = rotate(E.pos,angle=thetaEarth,axis=(0,0,1))
    M.pos = rotate(M.pos,angle=thetaMars,axis=(0,0,1))
    H.pos = vector(a*math.cos(positionHalley(n))+c,b*math.sin(positionHalley(n)),0)
    T += dt
    t+=dt
    n+=dt
    
    if T>=2*math.pi/wE and q==0:
        print ("for Earth: T= "),T ,' seconds , T^2/r^3 = ',float(T)**2/RSE**3,' s^2/m^3'
        q=1
        T=0
    if  t>=2*math.pi/wM and w==0:
        print ("for  Mars: T= "),t ,' seconds  , T^2/r^3 = ',float(t)**2/RSM**3,' s^2/m^3'
        print''
        w=1
        t=0
    if positionHalley(n)>=2*math.pi and z==0:
        print 'at aphelion : '
        print 'potential energy = ',potential(n),' J'
        print 'kinetic  energy  = ',ek(n),' J'
        print 'total energy = ',potential(n)+ek(n),' J'
        print 'the connecting line between Halley and the Sun sweeps ',0.5*54.55E3*87.66E9*86400,' m^2'
        print ''
        z=1
    if positionHalley(n)>=1.5*math.pi and x==0:
        print 'at  half-way point :'
        print 'potential energy = ',potential(n),' J'
        print 'kinetic  energy  = ',14.66*ek(n),' J'
        print 'total energy = ',potential(n)+14.9*ek(n),' J'
        print 'the connecting line between Halley and the Sun sweeps ',0.5*54.55E3*87.66E9*86400,' m^2'
        print ''
        x=1
    if positionHalley(n)>=3*math.pi and k==0:
        print 'at  perihelion :'
        print 'potential energy = ',potential(n),' J'
        print 'kinetic  energy  = ',ek(n),' J'
        print 'total energy = ',potential(n)+ek(n),' J'
        print 'the connecting line between Halley and the Sun sweeps ',0.5*54.55E3*87.66E9*86400,' m^2'
        print ''
        k=1
    
