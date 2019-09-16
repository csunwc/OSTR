from turtle import *
import time
import math

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check


radius=60  #default 60
petals=6   #default 6
arcAngle=60  # arc angle, default 60/360
arcSegLen=3 # arc segment len in mm

# draw_arc(radius)
def draw_arc(r):  # r: radius of arc
    c=2*math.pi*r # circumference of a full circle w/ given radius
    ca=c*(arcAngle/360)  # circumference of arc, a fraction of circle
    n=int(ca/arcSegLen)  # no of segments, round up to int
    for i in range(n):
        forward(arcSegLen) # draw a segment
        left(arcAngle/n) # turn fractional angle

# draw_petal(radius)
def draw_petal(r):
    pendown()
    time.sleep(0.5)
    draw_arc(r)  # 1st half
    left(180-arcAngle)  # point back to starting pt for line of symmetry
    draw_arc(r)  # 2nd half
    penup()
    time.sleep(0.5) 
    left(180-arcAngle)  # point back to starting pt for line of symmetry


# =========== MAIN ===================
penup()

#draw_arc(radius)
#draw_petal(radius)

#'''
for i in range(petals):
    draw_petal(radius)
    left(360/petals) # rotate into start pos for next petal
#'''

done()
