'''
def f(s, m, p):
    if s >= 62: return m%2 == 0
    if m == 0: return 0

    h = []
    if p != "+1": h+=[f(s+1, m-1, '+1')]
    if p != '+2': h+=[f(s+2, m-1, '+2')]
    if p != '*3': h+=[f(s*3, m-1, '*3')]

    return any(h) if(m-1)%2 == 0 else all(h)

print([s for s in range(1, 61+1) if f(s, 2, '')])#20
print([s for s in range(1, 61+1) if not f(s, 1, '') and f(s,3,'')])#7 19
print([s for s in range(1, 61+1) if not f(s,2,'') and f(s,4,'')])#6
'''
'''
def f(s,m):
    if 56<= s <= 80 : return m%2 == 0
    if s > 80: return (m-1)%2 == 0
    if m == 0: return 0

    h = [f(s+1, m-1), f(s*3,m-1)]

    return any(h) if (m-1)%2 == 0 else all(h)
print([s for s in range(1, 55+1) if f(s, 2)])#7
print([s for s in range(1,55+1) if not f(s,1) and f(s,3)])#18 53
print([s for s in range(1,55+1) if not f(s, 2) and f(s,4)])#52
'''
def f(s1, s2, m):
    if s1 + s2 <= 20: return m%2 == 0
    if m == 0: return 0

    h = [f(s1-1, s2, m-1), f((s1+1)//2, s2, m-1),
         f(s1, s2-1, m-1), f(s1, (s2+1)//2, m-1)]
    return any(h) if (m-1)%2 == 0 else all (h)

print([s for s in range(11, 200) if f(10, s, 2)])#21
print([s for s in range(11, 200)if not f(10, s, 1) and f(10,s,3)])#22 42
print([s for s in range(11,200) if not f(10, s, 2) and f(10,s, 4)])#24

