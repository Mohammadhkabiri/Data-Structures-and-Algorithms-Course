import heapq

n,m=map(int,input().split())
f=[];s=[]
for _ in range(n):
    x,y=map(int,input().split())
    f.append(x);s.append(y)

h=[];d={}
l=0
cs=0
ans=10**18

for r in range(n):
    cs+=f[r]
    heapq.heappush(h,(-s[r],r))
    while cs>=m:
        while h and d.get(h[0][1],0):
            d[h[0][1]]-=1
            heapq.heappop(h)
        ans=min(ans,-h[0][0])
        cs-=f[l]
        d[l]=d.get(l,0)+1
        l+=1

print(ans)
