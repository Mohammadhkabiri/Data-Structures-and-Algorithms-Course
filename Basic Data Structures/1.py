from collections import deque

n=int(input())
a=list(map(int,input().split()))
a.sort()
d=deque()

for x in reversed(a):
    if d:
        d.appendleft(d.pop())
    d.appendleft(x)

print(*d)
