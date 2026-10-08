'''
#1
def fib(x):
    if x <= 2:
        return 1
    return fib(x-1) + fib(x-2)
print(fib(8))

#2
def f(x, stop): #x - откуда, stop - где стоп
    if x == stop: return 1
    if x > stop: return 0
    return f(x+1, stop) + f(x+2, stop) + f(x*2, stop)
print(f(3, 10)* f(10,12))

#3
def f(x, stop):
    if x == stop: return 1
    if x > stop: return 0
    return f(x+1, stop) + f(x+3, stop)
print(f(1, 9)*f(9, 17))

#4
def f(x, stop):
    if x == stop: return 1
    if x > stop: return 0
    return f(x+1, stop) + f(x+3, stop)
print(f(1, 8)*f(8, 15))
'''

#5
def f(x, stop):
    if x == stop: return 1
    if x > stop: return 0
    if x == 25: return 0
    return f(x+1, stop) + f(x*2, stop)
print(f(2, 14) * f(14, 29))
