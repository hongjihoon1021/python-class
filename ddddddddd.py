from turtle import *
import random
color_= ['green','blue','red']
print('turtle')
while True:
    num=random.randrange(3, 110)
    coak= random.choice(color_)
    forward(num)
    circle(num)
    color(coak)
