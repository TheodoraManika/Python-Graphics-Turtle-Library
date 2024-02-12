from turtle import *
import random

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for i in range(360): 
    pencolor(colors[i % 6])
    forward(i)
    left(59)