#1
'''
a = int(input())

def sumCh(a):
    s = 0
    while a != 0:
        s+= a%10
        a=a//10
    return s

k = sumCh(a)
print(k)
'''
#2
'''
print('Введите два натуральных числа:')
a, b = map(int, input().split())
'''

def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a% b
        else:
            b = b%a
    return (a+b)
'''
s = NOD(a,b)
print(f'НОД({a},{b}) = {s}')

#2

print('Введите натуральное число:')
a = int(input())

def revers (a):
    s = 0
    while a != 0:
        s = s*10 + a%10
        a = a//10
    return (s)
ch = revers(a)
print(f'После перворота: {ch}.')
'''
#3
a, b = map(int, input().split())

def NOK (a, b):
    N = int(a*b / NOD(a,b))
    return (N)

N = NOK(a,b)
print(N)

        
