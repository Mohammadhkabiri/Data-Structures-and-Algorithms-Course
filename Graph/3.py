
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

vis = [False] * (n + 1)

def dfs(s):
    st = [s]
    vis[s] = True
    while st:
        x = st.pop()
        for y in g[x]:
            if not vis[y]:
                vis[y] = True
                st.append(y)

c = 0
for i in range(1, n + 1):
    if not vis[i]:
        dfs(i)
        c += 1

print(c - 1)
