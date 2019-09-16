from turtle import *
import time

pensize(5)          # pensize & color are not implemented in robot
pencolor('skyblue')  # but for simulation check

side=20


pendown()

for i in range (1,50):
  forward(side)
  left(92)
  side=side+7

penup()
time.sleep(1)

done()
