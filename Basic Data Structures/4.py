import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())

p = {}
nxt = {}

for i, x in enumerate(a):
    if i > 0:
        p[x] = a[i - 1]
    if i < n - 1:
        nxt[x] = a[i + 1]

h = a[0]  

for _ in range(q):
    t = tuple(map(int, input().split()))
    if t[0] == 1:
        _, x, y = t
  
        z = nxt.get(x) 
        nxt[x] = y
        p[y] = x
        if z is not None:
            nxt[y] = z
            p[z] = y
    
    else:
        _, x = t
        u = p.get(x) 
        v = nxt.get(x) 
        if u is None:
            h = v
            if v is not None:
                p[v] = None
        else:
            nxt[u] = v
        if v is not None:
            p[v] = u

        if x in p:
            del p[x]
        if x in nxt:
            del nxt[x]


res = []
cur = h
while cur is not None:
    res.append(cur)
    cur = nxt.get(cur) 
print(*res)
