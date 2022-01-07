import sys
m = list(i[:-1].split(' ') for i in sys.stdin.readlines())
e = []
for i in m:
    e.append(i[-1])
s = []
for i in range(len(e)):
    p = e[i].capitalize()
    s.append(p)
f = set(s)
d = ', '.join(f)
print(d)
