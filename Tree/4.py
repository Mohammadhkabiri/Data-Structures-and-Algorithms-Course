import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

queries = []
for i in range(q):
    l, r = map(int, input().split())
    queries.append((r, l, i))

queries.sort()

bit = [0] * (n + 2)

def update(i, v):
    while i <= n:
        bit[i] += v
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

last = {}
ans = [0] * q
cur = 1

for r, l, idx in queries:
    while cur <= r:
        x = a[cur]
        if x in last:
            update(last[x], -1)
        update(cur, 1)
        last[x] = cur
        cur += 1
    ans[idx] = query(r) - query(l - 1)

print("\n".join(map(str, ans)))
