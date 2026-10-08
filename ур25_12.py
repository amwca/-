'''
print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x<=y) and (y<=z)
            if f == 0:
                print(x,y,z)

#1
from itertools import *
#product - всевозиожныее комбинации
#permutations - всевозможные перестановки
def f(x, y, z):
    return (x<=y) and (y<=z)
#неполная таблица истонности из усл
table = [(1, 0, 0),
         (1, 0, 1)]

for s in permutations('xyz'):
    if [f(**dict(zip(s,row)))for row in table] == [0,1]:
        print(*s, sep = '')        
'''

#2
from itertools import *

table = [(0, 0, 0),
         (1, 0, 0),
         (1, 1, 0)]

def f(x, y, z):
    return ((not x) and y and z) or ((not x) and (not z))

for s in permutations('xyz'):
    if [f(**dict(zip(s, row)))for row in table] == [1, 1, 1]:
        print(*s, sep = '')

