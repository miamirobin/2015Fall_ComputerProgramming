from visual import *
from visual.graph import*
import math
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = display(title='Spring Wave', width=1200, height=300, background=(0.5,0.5,0), range = N*d/2+0.5, center = ((N-1)*d/2, 0, 0))
balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]#3
springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)]#3
c = curve(display = scene)
#Unit_K, n = 2 * pi/(N*d), 10
#Wavevector = n * Unit_K

#phase = Wavevector * arange(N) * d
#ball_pos, ball_orig, ball_v, spring_len = arange(N)*d + A*sin(phase), arange(N)*d, zeros(N), ones(N)*d
scene2=gdisplay(y=400,width=800,height=300, xtitle='Wavevector',ytitle='angular frequency',background=(0.4,0.4,0))
p=gcurve(color=color.cyan,gdisplay=scene2)

t, dt = 0, 0.001
for n in range(1,26):
    
    if n==25:
        n=26
    A, N, omega = 0.10, 50, 2*pi/1.0
    size, m, k, d = 0.06, 0.1, 10.0, 0.4
    #balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)]#3
    #springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)]#3
    #c = curve(display = scene)
    Unit_K  = 2 * pi/(N*d)
    Wavevector = n * Unit_K

    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = arange(N)*d + A*sin(phase), arange(N)*d, zeros(N), ones(N)*d
    
    t, dt = 0, 0.001

    while True:
        rate(1000)
        t += dt
        #
        spring_len[0:-1] =ball_pos[1:]-ball_pos[0:-1]
    
        ball_v[1:] +=k*(spring_len[1:]-d)/m*dt-k*(spring_len[0:-1]-d)/m*dt#6 
        ball_pos[0] +=(k*(spring_len[0]-d)/m*dt)*dt
        ball_pos[1:] +=ball_v[1:]*dt
        for i in range(N):
            balls[i].pos.x = ball_pos[i]#3
        for i in range(N-1):
            springs[i].pos = balls[i].pos#3
            springs[i].axis = balls[i+1].pos-balls[i].pos
        ball_disp = ball_pos-ball_orig
        c.x = ball_orig
        c.y = ball_disp * 4.0 + 1.0
        if (n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==10 or n==11 or n==12 or n==13 or n==14 or n==15 or n==16 ) and ball_v[50/n-1]<=0:
            T= 2*t
            print 'n= ',n,'  T= ',T,' S'
            t=0
            p.plot(pos=(Wavevector, 2*math.pi/T))
            break
        if ( n==17 or n==18 or n==19 or n==20 or n==21 or n==22 or n==23 or n==24 ) and ball_v[50/n-1]>=0:
            T= 2*t
            print 'n= ',n,'  T= ',T,' S'
            t=0
            p.plot(pos=(Wavevector, 2*math.pi/T))
            break
        if n==1 and ball_v[12]>=0:
            T= 2*t
            print 'n= ',n,'  T= ',T,' S'
            t=0
            p.plot(pos=(Wavevector, 2*math.pi/T))
            break
        if n==26 and ball_v[2]>=0:
            T= 2*t
            print 'n= ',25,'  T= ',T,' S'
            t=0
            n=25
            p.plot(pos=(Wavevector, 2*math.pi/T))
            break
        
            
        
