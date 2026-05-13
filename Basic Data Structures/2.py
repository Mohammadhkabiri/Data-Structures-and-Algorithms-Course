n=int(input())
a=list(map(int,input().split()))
s=[]
m=0
for i,x in enumerate(a+[0]):
    while s and a[s[-1]]>x:
        h=a[s.pop()]
        l=s[-1] if s else -1
        m=max(m,h*(i-l-1))
    s.append(i)
print(m)
