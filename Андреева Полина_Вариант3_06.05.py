#1

a = [int(x) for x in open('17_9.txt')]
res = []
for i in range(len(a)):
    if a[i]%10 + (a[i]//10)%10 >=15:
        if a[i]%3 !=0 and a[i]%4 != 0 and a[i]%7 !=0:
            res.append(a[i])
print(min(res), sum(res))
#Ответ: 1189 460004

#2

a = [int(x) for x in open('17_10.txt')]
res = []
for i in range(len(a)-1):
    if a[i]*a[i+1] > 0:
        if (a[i]+a[i+1])%7 == 0:
            res.append(a[i]*a[i+1])
print(len(res), min(res))
#Ответ: 359 115022

#3

a = [int(x) for x in open('17_11.txt')]
res = []
for i in range(len(a)-2):
    if ((a[i]%12 == 0)+
        (a[i+1]%12 == 0)+
        (a[i+2]%12 == 0))>= 1:
        if a[i]%3 == 0 and a[i+1]%3 == 0 and a[i+2]%3 == 0:
            res.append((a[i]+a[i+1]+a[i+2])/3)
print(len(res), min(res))
#Ответ: 119 -7213.0

#4

a = [int(x) for x in open('17_12.txt')]
res = []
osob = min(x for x in a if x%6 == 0)
for i in range(len(a)-1):
    if a[i]%osob == 0 and a[i+1]%osob == 0:
        res.append(a[i]+a[i+1])
print(len(res), max(res))
#Ответ: 17 172728

#5
a = [int(x) for x in open('17_19.txt')]
res = []
osob = max(x for x in a if 1000<=abs(x)<=9999 and abs(x)%100 == 43)

for i in range(len(a)-1):
    if 1000<=abs(a[i])<=9999 or 1000<=abs(a[i+1])<=9999:
        if (a[i]+a[i+1])**2 < osob**2:
            res.append((a[i]+a[i+1])**2)
print(len(res), max(res))
#Ответ: 1218 98843364





        
