from turtle import *
import time

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check

length = 10         # image size var

pendown()

for i in range(20):
    forward(i * length)
    right(144)

penup()
time.sleep(1)

done()
