'''
n = 5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3
c0 = 0
while n > 0:
    if n % 7 == 0: c0+=1
    n = n // 7
print(c0)

n = (2**345 + 8**65 - 4**130)*(8**123 - 2**89 + 4**45)
summ = 0
while n > 0:
    summ += n %8
    n = n // 8
print(summ)

for x in range (1000):
    n = 3 * 7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 1*7**(2*x)
    summ = 0
    while n > 0:
        summ = summ + n%7
        n = n // 7
    if summ == 18:
        print(x)
        break

for x in range (2100):
    n = 4**1014 - 2**x + 12
    c0 = 0
    while n > 0:
        if n % 2 == 0:
            c0 += 1
        n = n // 2
    if c0 == 2000:
        print(x)
        break

for x in range (3000, -1, -1):
    n = 9*11**210 + 8*11**150 - x
    c0 = 0
    while n > 0:
        if n % 11 == 0:
            c0 += 1
        n = n // 11
    if c0 == 60:
        print(x)
        break
'''
for x in range (28, -1, -1):
    n = int('9230874', 29) + x*29**3+\
        int('52406152', 29) + x*29**4
    if n % 28 == 0:
        print(n//28)
        break











