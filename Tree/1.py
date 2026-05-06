import sys

def f1(ranges, total, dist):
    cnt = 1
    last = ranges[0][0]
    idx = 0
    x, y = ranges[idx]
    
    while cnt < total:
        nxt = last + dist
        
        while idx < len(ranges) and nxt > y:
            idx += 1
            if idx < len(ranges):
                x, y = ranges[idx]
            else:
                return False
        
        if nxt < x:
            nxt = x
        
        if x <= nxt <= y:
            cnt += 1
            last = nxt
        else:
            idx += 1
            if idx < len(ranges):
                x, y = ranges[idx]
                nxt = x
                cnt += 1
                last = nxt
            else:
                return False
    
    return cnt >= total

def f2(total, cnt, ranges):
    ranges.sort()
    left = 1
    right = 0
    
    for a, b in ranges:
        right = max(right, b - a)
    
    if len(ranges) > 1:
        right = max(right, ranges[-1][1] - ranges[0][0])
    
    right = max(right, (ranges[-1][1] - ranges[0][0]) // (total - 1) + 1)
    
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if f1(ranges, total, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    intervals = []
    p = 2
    for _ in range(k):
        a = int(data[p])
        b = int(data[p + 1])
        intervals.append((a, b))
        p += 2
    result = f2(n, k, intervals)
    print(result)

if __name__ == "__main__":
    main()
