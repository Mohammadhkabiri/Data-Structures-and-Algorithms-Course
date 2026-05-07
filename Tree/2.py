def build_kmp_table(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return 0
    n = len(text)
    m = len(pattern)
    lps = build_kmp_table(pattern)
    count = 0
    i = 0  
    j = 0 
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    w = int(data[1])
    
    a = list(map(int, data[2:2 + n]))
    b = list(map(int, data[2 + n:2 + n + w]))
    
    if w == 1:
        print(n)
        return
    
    diff_a = [a[i + 1] - a[i] for i in range(n - 1)]
    diff_b = [b[i + 1] - b[i] for i in range(w - 1)]
    
    result = kmp_search(diff_a, diff_b)
    print(result)

if __name__ == "__main__":
    main()
