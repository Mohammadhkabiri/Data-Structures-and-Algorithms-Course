import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(input().strip()) for _ in range(n)]

sx = sy = tx = ty = -1

for i in range(n):
    for j in range(m):
        if g[i][j] == 'A':
            sx, sy = i, j
        elif g[i][j] == 'B':
            tx, ty = i, j

vis = [[False]*m for _ in range(n)]
q = deque()
q.append((sx, sy))
vis[sx][sy] = True

d = [(1,0),(-1,0),(0,1),(0,-1)]

ok = False

while q:
    x, y = q.popleft()
    if (x, y) == (tx, ty):
        ok = True
        break
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if not vis[nx][ny] and g[nx][ny] != '#':
                vis[nx][ny] = True
                q.append((nx, ny))

print("YES" if ok else "NO")
