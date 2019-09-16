from turtle import *
import time
import math

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check

radius=30

def draw_polygon(r, sides): # r: radius
    # calc turn angle in deg
    angle=360/sides
    # calc side length
    length= 2* r * math.sin(math.radians(angle/2))
    # draw shape
    for i in range(sides):
        forward(length)
        left(angle)


arcSegLen=3 # arc segment len in mm

# draw circle by approx it with a polygon with very small sides
def draw_circle(r , arc = 360):  # r: radius of, arc: deg arc or partial circle

   # calc number of steps based on circumference rather than angle
    c = 2 * math.pi * r  # circumference of a full circle w/ given radius
    ca = c * abs(arc / 360)  # circumference of arc, a fraction of circle
    n=int(ca/arcSegLen)  # no of segments, round up to int
    sa= abs(arc/n)  # segment ang
    for i in range(n):
        forward(arcSegLen) # draw a segment
        if arc >0:   # pos angle
            left(sa)  # left turn  CCW
        else: # neg angle
            right(sa) # CW



# =========== MAIN ===================

pendown()
time.sleep(0.5)

print(heading())
print(position())

draw_circle(radius)

# python circle() has a diff approach to neg arc
#circle(radius, 180)
#circle(radius, -180)

# figure 8
#draw_circle(radius, 180)
#draw_circle(radius, -360)
#draw_circle(radius, 180)

#draw_polygon(radius, 100)

print(heading())
print(position())

penup()
time.sleep(0.5)

done()
