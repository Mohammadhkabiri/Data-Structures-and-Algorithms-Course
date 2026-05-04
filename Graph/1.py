import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n+1)]
r = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    r[v].append(u)

def dfs(s, t, v):
    st = [s]
    v[s] = True
    while st:
        x = st.pop()
        for y in t[x]:
            if not v[y]:
                v[y] = True
                st.append(y)

v = [False]*(n+1)
dfs(1, g, v)

if not all(v[1:]):
    print("NO")
    exit()

v = [False]*(n+1)
dfs(1, r, v)

if not all(v[1:]):
    print("NO")
else:
    print("YES")
