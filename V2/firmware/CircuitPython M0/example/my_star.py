from turtle import *
import time

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check

length = 60         # image size

pendown()

for i in range(5):
    forward(length)
    right(144)

penup()
time.sleep(1)

done()
