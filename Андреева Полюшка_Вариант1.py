#1
'''
def f (n):
    r = bin(n)[2:]
    if r.count('1')%2 == 0:
        r = r + '01'
    else:
        r = r + '10'
    return int(r,2)

for n in range(1, 100):
    if f(n)>73:
        print(n)
        break

#Ответ: 19
'''
#2
'''
def f(n):
    r = bin(n)[2:]
    if r.count('1')%2 == 0: r = r + '00'
    else: r = r + '10'
    return int(r,2)

for n in range(1,200):
    if f(n) > 103:
        print(n)
        break
#Ответ: 26
'''
#3
'''
def f(n):
    r = bin(n)[2:]
    if r.count('1')%2 == 0: r = r + '11'
    else: r = r + '01'
    return int(r,2)

res = []
for n in range(1,200):
    r = f(n)
    if r > 31: res.append(r)
print(min(res))
#Ответ: 33
'''
#4
'''
def f(n):
    r = bin(n)[2:]
    if r.count('1')>r.count('0'): r = r + '0'
    else: r = '1' + r
    if r.count('1')>r.count('0'): r = r + '0'
    else: r = '1' + r
    return int(r,2)

for n in range(1, 400):
    if f(n) > 500:
        print(n)
        break
#Ответ: 126
'''
#5
def f(n):
    r = bin(n)[2:]
    r = r[1:]
    if r.count('1')%2 == 0: r = '10' + r
    else: r = '1' + r + '0'
    return int(r,2)

#print(f(4), f(6))
res = []
for n in range(2, 1000):
    r = f(n)
    if r < 450:
        res.append(r)
print(max(res))
#Ответ: 444









