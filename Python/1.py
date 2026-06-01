board = [list(input().strip()) for _ in range(3)]

solo = set()
duo = set()

for i in range(3):
    r = board[i]
    u = set(r)
    if len(u) == 1:
        solo.add(r[0])
    elif len(u) == 2:
        p = tuple(sorted(u))
        duo.add(p)

for j in range(3):
    c = [board[i][j] for i in range(3)]
    u = set(c)
    if len(u) == 1:
        solo.add(c[0])
    elif len(u) == 2:
        p = tuple(sorted(u))
        duo.add(p)

d1 = [board[i][i] for i in range(3)]
u = set(d1)
if len(u) == 1:
    solo.add(d1[0])
elif len(u) == 2:
    p = tuple(sorted(u))
    duo.add(p)

d2 = [board[i][2-i] for i in range(3)]
u = set(d2)
if len(u) == 1:
    solo.add(d2[0])
elif len(u) == 2:
    p = tuple(sorted(u))
    duo.add(p)

print(len(solo))
print(len(duo))
