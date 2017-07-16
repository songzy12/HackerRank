T = int(raw_input())

def compute_parity(a, n):
    visited = [False] * (n+1)
    ans = 0
    for i, t in enumerate(a):
        if visited[t]:
            continue
        cur = 0
        j = i 
        while not visited[a[j]]:
            visited[a[j]] = True
            cur += 1
            j = a[j]
        ans += cur - 1
    return ans
            

for t in range(T):
    N = int(raw_input())
    a = [0] + [int(x) for x in raw_input().split()]
    print 'YES' if compute_parity(a, N) % 2 == 0 else 'NO'
    
