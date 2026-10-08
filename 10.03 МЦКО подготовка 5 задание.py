#1
'''
def f(n):
    r = bin(n)[2:]
    if r.count('1')% 2 == 0: #кол-во вхождений подстрок в строку
        r = r + '0'
    else: r = r + '1'
    r = r + '0'
    return int(r, 2)

res = []
for N in range(1, 100):
    r = f(N)
    if r > 130:
        res.append(r)
print(min(res))
'''

#2
'''
def f(n):
    r = bin(n)[2:] #отбрасываем служ симаолы
    r = r + r[-1]
    if r.count('1')%2 == 0: r = r + '00'
    else: r = r + '10'
    return int(r,2)

for N in range (1, 20):
    if f(N) > 97:
        print(N)
        break
'''
#4
'''
def f (n):
    r = bin(n)[2:]
    k = r.count('1')
    r = r + str(k%2)
    r += '0'
    return int(r,2)


res = []
for N in range(1, 200):
    r = f(N)
    if 210<=r<= 260:
        res.append(r)
print(len(set(res)))
'''

#5
'''
def f(n):
    r = bin(n)[2:]
    if n % 2 == 1: r = '1' + r + '11'
    else: r = '11' + r + '00'
    return int(r,2)

res = []
for N in range (1, 100):
    r = f(N)
    if r < 127:
        res.append(r)
print(max(res))
'''
#6
'''
def f(n):
    r = bin(n)[2:]
    if r.count('1')%2 == 0:
        r = r + '0'
        r = '10' + r[2:]
    else:
        r = r + '1'
        r = '11' + r[2:]
    return int(r,2)

for n in range(1,100):
    if f(n)>= 16:
        print(n)
        break
'''
#7
'''
def f(n):
    r = oct(n)[2:]
    if n%5 == 0: r = r + r[:3]
    else:
        ost = bin(n%5)[2:]
        r = r + ost
    return int(r,8)

for n in range(11, 10000):
    if f(n) >= 35000:
        print(n)
        break
'''
#8
'''
def f(n):
    r = hex(n)[2:]
    if r.count('b')%2 == 0: r = '1' + r
    else: r = r + '1'
    return int(r,16)

res = []
for n in range(1,100):
    if 9<f(n)<100:
        res.append(n)
print(len(res))
'''
#9
'''
def n3(n):
    if n == 0: return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n // 3
    return(s)

def f (n):
    r = n3(n)
    if n % 3 == 0: r = '1' + r + '02'
    else:
        ost = n3((n%3)*4)
        r = r + ost
    return int(r,3)

for n in range(200, 0, -1):
    if f(n)<199:
        print(n)
        break
'''
def n12 (n):
    s = ''
    while n > 0:
        ost = n %12
        if ost == 10: s = 'a' +s
        elif ost == 11: s = 'b' +s
        else: s = str(ost) + s
        n //= 12
    return(s)
def f (n):
    r = n12(n)
    if n % 12 == 0: r = r + r[-2:]
    else:
        ost = n12((n%12)*9)
        r = r + ost
    return int(r,12)

res = []
for n in range(1, 300):
    r = f(n)
    if r > 300:
        res.append(r)
print(min(res))













