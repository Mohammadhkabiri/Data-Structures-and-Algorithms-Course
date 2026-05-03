import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

seen = set()

for _ in range(m):
    u, v = map(int, input().split())
    if u == v:   
        continue
    if u > v:
        u, v = v, u
    if (u, v) in seen:  
        continue
    seen.add((u, v))
    g[u].append(v)
    g[v].append(u)

vis = [False] * (n + 1)
ok = False

def dfs(s):
    global ok
    st = [(s, -1)]
    vis[s] = True
    while st:
        x, p = st.pop()
        for y in g[x]:
            if not vis[y]:
                vis[y] = True
                st.append((y, x))
            elif y != p:
                ok = True
                return

for i in range(1, n + 1):
    if not vis[i]:
        dfs(i)
        if ok:
            break

print("YES" if ok else "NO")
