#1
'''
a = [int(x) for x in open('17-4310.txt')]
res = []
for i in range(len(a)):
    if a[i]%3 == 0 and a[i]%7 != 0 and a[i]%17 != 0 and a[i]%19 != 0 and a[i]%27 != 0:
        res.append(a[i])

print(len(res), max(res))
'''
#2
'''
a = [int(x) for x in open('17-4322.txt')]
res = []

for i in range(len(a)):
    if a[i] % 10 == 5 or a[i]%10 == 7:
        if a[i] % 9 != 0 and a[i] % 11 != 0:
            res.append(a[i])
print(len(res), max(res)+min(res))
'''
#3
'''
a = [int(x) for x in open('17-4301.txt')]
res = []
for i in range(len(a)-1):
    if a[i]*a[i+1] > 0:
        if (a[i] + a[i+1]) %7 == 0:
            res.append(a[i]*a[i+1])
print(len(res), min(res))
'''
#4
'''
a = [int(x) for x in open('17-4353.txt')]
res = []
for i in range(len(a)-1):
    if abs(a[i])%10 == 5 and abs(a[i+1])%10 == 5:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
'''
#5
'''
a = [int(x) for x in open('17-4659.txt')]
osob = sum(a)/len(a) # среднее арифметическое
res = []
for i in range(len(a)-1):
    if a[i] < osob and a[i+1] < osob:
        if (a[i]+a[i+1]) % 100 == 19:
            res.append(a[i]+a[i+1])
print(len(res), min(res))
'''
#6
'''
a = [int(x)for x in open('17-4690.txt')]
osob = max([x for x in a if x%71 == 0])
res = []
for i in range(len(a)-1):
    if a[i] < osob and a[i+1] < osob:
        if a[i]%13 == 0 or a[i+1] % 13 == 0:
            res.append(a[i]+a[i+1])
print(len(res), min(res))
'''
#7
'''
a = [int(x) for x in open('17-5055.txt')]
osob = min(x for x in a if x % 17 == 0)
res = []
for i in range(len(a)-1):
    if a[i]%osob == 0 or a[i+1]%osob == 0:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
'''
#ДЕМО МЦКО
a = [int(x) for x in open('13.txt')]
osob = min(x for x in a if x % 15 != 0)
res = []
for i in range(len(a)-1):
    if a[i] % osob == 0 and a[i+1]%osob == 0:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
















