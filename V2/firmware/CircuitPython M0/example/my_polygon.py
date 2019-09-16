from turtle import *
import time

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check

num_sides = 8
side_length = 30
angle = 360.0 / num_sides


pendown()

for i in range(num_sides):
    forward(side_length)
    right(angle)

penup()
time.sleep(1)

done()
