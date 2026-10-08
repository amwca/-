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












