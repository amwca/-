'''
Андреева Полина Вариант 2
'''
#1
'''
def f(s, m):
    if s >= 30 : return m%2 == 0
    if m == 0: return 0

    h = [f(s+2,m-1), f(s*2, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(1,29+1) if f(s,2)])#13
print([s for s in range(1,29+1) if not f(s,1) and f(s,3)])#3
print([s for s in range(1,29+1) if not f(s,2) and f(s,4)])#9 10
'''
#2

def f(s, m):
    if 20<=s<=30: return m%2 == 0
    if s > 30: return (m-1)%2 == 0
    if m == 0: return 0

    h = [f(s+1, m-1), f(s*2, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h)
print([s for s in range(1, 19+1) if f(s,2)])#18
print([s for s in range(1, 19+1) if not f(s,1) and f(s,3)])
print([s for s in range(1, 19+1) if not f(s,2) and f(s,4)])#16

#3
'''
def f(s, m, p):
    if s>=68: return m%2 == 0
    if m == 0: return 0

    h = []
    if p!='+1': h+=[f(s+1, m-1, '+1')]
    if p!='+2': h+=[f(s+2, m-1, '+2')]
    if p!='*2': h+=[f(s*2, m-1, '*2')]

    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(1,67+1) if f(s,2, '')])#33
print([s for s in range(1,67+1) if not f(s, 1, '') and f(s,3, '')])#17 32
print([s for s in range(1,67+1) if not f(s, 2, '') and f(s,4, '')])#16
'''
#4
'''
def f(s1, s2, m):
    if s1+s2 >= 66: return m%2 == 0
    if m == 0: return 0

    h = [f(s1+2, s2, m-1), f(s1*2, s2, m-1),
         f(s1, s2+2, m-1), f(s1, s2*2, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(1, 58+1) if f(7, s, 2)])#15
print([s for s in range(1, 58+1) if not f(7, s, 1) and f(7, s, 3)])#25
print([s for s in range(1, 58+1) if not f(7, s, 2) and f(7, s, 4)])#23 26
'''
#5
'''
def f(s1, s2, m):
    if s1+s2 <= 32: return m%2 == 0
    if m == 0: return 0

    h = [f(s1-1, s2, m-1), f((s1+1)//2, s2, m-1),
         f(s1, s2-1, m-1), f(s1, (s2+1)//2, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h)
print([s for s in range(23, 200) if f(10, s, 2)])#45
print([s for s in range(23, 200) if not f(10, s, 1) and f(10, s, 3)])#46 90
print([s for s in range(23, 200) if not f(10, s, 2) and f(10, s, 4)])#48
'''


