#1
'''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 10

for _ in range(100):
    fd(10*k); rt(30)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k, y*k); dot(6,'pink')

exitonclick()
'''
#2
'''
from turtle import*
screensize(2000,2000)
tracer(15)
lt(90)
k = 10

for _ in range(100):
    fd(10*k); rt(8)

up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(4, 'pink')
exitonclick()
'''
#3
'''
from turtle import*
screensize(2000,2000)
tracer(15)
lt(90)
k = 60

for _ in range(16):
    lt(36); fd(4*k); lt(36)

up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#4
'''
from turtle import*
screensize(2000,2000)
tracer(15)
lt(90)
k = 60

for _ in range(14):
    for _ in range (3):
        fd(3*k); rt(90)
    lt(180)

up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#5
'''
from turtle import*
screensize(2000,2000)
tracer(0)
lt(90)
k = 50

fd(9*k)
rt(90)
for _ in range(2):
    fd(3*k); rt(90); fd(3*k); rt(270)
for _ in range (2):
    fd(3*k); rt(90)
fd(9*k)

up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#6
'''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 30

for _ in range(15):
    fd(7*k); rt(30); fd(8*k); rt(150)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k, y*k); dot(6,'pink')

exitonclick()
'''
#7
'''
from turtle import*
screensize(2000,2000)
tracer(0)
lt(90)
k = 30

for _ in range(8):
    for _ in range (4):
        fd(5*k); rt(30);fd(6*k); rt(150)
    rt(60)

up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#8
'''
from turtle import*
screensize(2000,2000)
tracer(0)
lt(90)
k = 40


for _ in range(3):
    fd(7*k); rt(90)
fd(8*k)
for _ in range (3):
    lt(90); fd(5*k)


up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#9
'''
from turtle import*
screensize(2000,2000)
tracer(0)
lt(90)
k = 20


for _ in range(5):
    fd(15*k); lt(90); fd(25*k); lt(90)
up()
fd(4*k); lt(90); fd(12*k); lt(90)
down()
for _ in range (6):
    fd(38*k); rt(90); fd(22*k); rt(90)


up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()
'''
#10
from turtle import*
screensize(2000,2000)
tracer(0)
lt(90)
k = 20
up()

for _ in range(3):
    down()
    for _ in range(2):
        fd(7*k); rt(90); fd(7*k); rt(90)
    up()
    fd(6*k); rt(90); fd(6*k); lt(90)


up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(5, 'pink')
exitonclick()


