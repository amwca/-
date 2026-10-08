#1
'''
a = [int(x) for x in open('17_29349.txt')]
res = []
mi = min(x for x in a if x > 0 and x%123 == 0)
for i in range(len(a)-1):
    if a[i]+a[i+1] < mi:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
'''
#2
'''
a = [int(x) for x in open('17_28762.txt')]
res = []
mi = min(x for x in a if x % 23 == 0)
for i in range(len(a)-1):
    if a[i]%mi == 0 or a[i+1] % mi == 0:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
'''
#3
a = [int(x) for x in open('17_28938.txt')]
res = []
osob = max(x for x in a if x%100 == 28)
for i in range(len(a)-2):
    if 99 < abs(a[i]) < 1000 or 99 < abs(a[i+1]) < 1000 or 99 < abs(a[i+2]) < 1000:
        sr = (a[i]+a[i+1]+a[i+2])/3
        if sr > 0 and sr < osob:
            res.append(a[i]+a[i+1]+a[i+2])
print(len(res), max(res))
   
