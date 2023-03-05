#!/bin/python3

n = int(input().strip())
cur = 0
ans = None

for i in range(1, n + 1):
    if n % i == 0:
        temp = sum(map(int, str(i)))
        if temp > cur:
            cur = temp
            ans = i
print(ans)
