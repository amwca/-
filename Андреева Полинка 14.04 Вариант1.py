#1
'''
from itertools import *
cnt = 0
for s in product('0123456789abcde', repeat = 5):
    s = ''.join(s)
    if s[0] != '0':
        for x in 'abcde':
            s = s.replace(x, '*')
        if s.count('8')==1 and s.count('*') >= 2:
            cnt+=1
print(cnt)
#Ответ: 83175
'''
#2
'''
from itertools import *
cnt = 0
for s in product('01234567', repeat = 6):
    s = ''.join(s)
    if s[0]!= '0':
        if s[0] not in '1357' and s[-1] not in '23' and  s.count('1') >=2:
            cnt += 1
print(cnt)
#Ответ:9930
'''
#3
'''
from itertools import *
cnt = 0
for s in product('аборсуэ', repeat = 5):
    s = ''.join(s)
    if s.count('у') == 0 and s.count('р')>=2:
        for x in 'р':
            s = s.replace(x, '*')
        for x in 'абосуэ':
            s = s.replace(x, '+')
        if '*+*' in s:
            cnt+=1
print(cnt)
#Ответ: 515
'''
#4
'''
from itertools import *
cnt = 0
for s in permutations('кобура'):
    s = ''.join(s)
    for x in 'кбр':
        s = s.replace(x, '-')
    for x in 'оуа':
        s = s.replace(x, '+')
    if '+-+-+-'== s or '-+-+-+' == s:
        cnt+=1
print(cnt)
#Ответ: 72
'''
#5
from itertools import *
cnt = 0
for s in set(permutations('шарлатан')):
    s = ''.join(s)
    for x in 'шрлтн':
        s = s.replace(x, '-')
    for x in 'а':
        s = s.replace(x, '+')
    if '++' in s or '--' in s:
        cnt+=1
print(cnt)
#Ответ: 
    












