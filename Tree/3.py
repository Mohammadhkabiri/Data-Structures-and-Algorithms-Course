import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    people = []
    idx = 1
    for i in range(n):
        a = int(data[idx])
        t = int(data[idx + 1])
        people.append((a, t, i)) 
        idx += 2
    
 
    people.sort(key=lambda x: x[0])
    

    heap = []
    
    current_time = 0
    max_wait = 0
    ptr = 0  
    
    while ptr < n or heap:
 
        if not heap:
            current_time = max(current_time, people[ptr][0])
        

        while ptr < n and people[ptr][0] <= current_time:
            a, t, priority = people[ptr]
            heapq.heappush(heap, (priority, a, t))  
            ptr += 1
        
   
        priority, a, t = heapq.heappop(heap)
        
 
        wait_time = max(0, current_time - a)
        max_wait = max(max_wait, wait_time)
        

        current_time += t
    
    print(max_wait)

if __name__ == "__main__":
    main()
