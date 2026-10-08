#1
'''
from turtle import *
screensize(2000, 2000)
tracer(0) #отключение анимации
lt(90) #left(90)- повернуть влево на 90 градусов
k = 30 #масштаб
for _ in range(5):
    rt(45) #right(45) - поворот вправо на 45 градусов
    fd(10*k) #forward - вперед на 10 шагов
    rt(45)
for _ in range(6):
    fd(20*k); rt(90)

up() #поднять хвост
#сетка
for x in range (-20, 20):
    for y in range (-20, 20):
        goto(x*k, y*k) #перейти в точку с координатами ху
        dot(4, 'pink') #поставить точку диаметром 4 и роховым цветом
exitonclick() #чтобы не закрылос окно
#площадь перечсечения фигур - половина квадрата со стороной 10
print(10*10/2)
'''

#2
'''''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 20
for _ in range(2):
    fd(13*k); rt(90); fd(20*k); rt(90)
up()
fd(8*k); rt(90); bk(3*k); lt(90)
down()
for _ in range(2):
    fd(16*k); rt(90); fd(8*k); rt(90)
up()
#cetka
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k); dot(4, 'pink')
exitonclick()
#количество точек внутри фигур = количество первой фигуры + кол-во точек второй - кол-во точек в персееч
print((13+1)*(20+1)+(16+1)*(8+1)-(6*6))
'''''
#3
'''''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 30

for _ in range(3):
    fd(5*k); lt(270); fd(9*k); rt(90)
lt (315)
for _ in range(4):
    fd(11*k); rt(90); fd(5*k); lt(270)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k, y*k); dot(6, 'pink')
exitonclick()
'''''
#4
'''''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 30

rt(90)
for _ in range(3):
    rt(45); fd(10*k); rt(45)
rt(315); fd(10*k)
for _ in range(2):
    rt(90), fd(10*k)

up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(40, 'plum')
exitonclick()
'''''
#5
'''''
from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k = 30

for _ in range(14):
    for _ in range(3):
        fd(3*k); rt(90)
    lt(180)
up()

for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(6, 'red')
exitonclick()
'''''

#6
'''''
from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30

for _ in range(3):
    fd(7*k); rt(90); fd(12*k); rt(90)
up()
fd(4*k); rt(90); fd(6*k); lt(90)
down()

for _ in range(4):
    fd(83*k); rt(90); fd(77*k); rt(90)
up()

for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(6, 'red')
exitonclick()
print(8*13 + 84*78 - 28)
'''''
#7
'''''
from turtle import *
screensize(2000, 2000)
tracer(0)
k = 40

for _ in range(10):
    goto(xcor()+ 3*k, ycor()+6*k)
    goto(xcor() + 7*k, ycor() -2*k)
    goto(xcor() -10*k, ycor() -4*k)

up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(6, 'red')
exitonclick()
'''''
#8
'''''
from turtle import *
screensize(2000, 2000)
tracer(0)
k = 40

for _ in range(2):
    goto(xcor() + 3 * k, ycor() + 4 * k)
    goto(xcor() - 3 * k, ycor() + 4 * k)
    goto(xcor() - 3 * k, ycor() - 4 * k)
    goto(xcor() + 3 * k, ycor() - 4 * k)

up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(6, 'red')
exitonclick()
'''''

#9
from turtle import *
screensize(2000, 2000)
tracer(0)
k = 30

for _ in range(2):
    goto(xcor() + 0 * k, ycor() + 12 * k)
    goto(xcor() + 5 * k, ycor() - 12 * k)
    goto(xcor() - 10 * k, ycor() + 0 * k)
    goto(xcor() + 5 * k, ycor() + 12 * k)
    goto(xcor() + 0 * k, ycor() + 4 * k)
    goto(xcor() + 3 * k, ycor() - 4 * k)
    goto(xcor() - 6 * k, ycor() + 0 * k)
    goto(xcor() + 3 * k, ycor() + 4 * k)

up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*k, y*k); dot(6, 'red')
exitonclick()
