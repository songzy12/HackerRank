T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    import math
    d = math.gcd(m, n)
    print(int(m / d * n / d))
