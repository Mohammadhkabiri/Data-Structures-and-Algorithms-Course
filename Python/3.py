x = input().strip()

if x == x[::-1]:
    print("YES")
else:
    y = x.rstrip('0')
    if y == y[::-1]:
        print("YES")
    else:
        print("NO")
