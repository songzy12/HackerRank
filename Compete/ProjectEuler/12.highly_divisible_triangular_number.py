# https://www.hackerrank.com/contests/projecteuler/challenges/euler012

MAXN = 1000
from math import sqrt, ceil

factors = {1: {}}
cnt = {1: 1}
n = 2
while True:
    factors[n] = {}
    for t in range(2, ceil(sqrt(n)) + 1):  # note this sqrt function
        if n % t != 0:
            continue
        if t * t > n:
            continue
        A = factors[t]
        B = factors[n // t]
        factors[n] = {x: A.get(x, 0) + B.get(x, 0) for x in set(A).union(B)}
        break
    else:
        factors[n] = {n: 1}

    temp = 1
    A = factors[n]
    B = factors[n - 1]
    for k, v in {x: A.get(x, 0) + B.get(x, 0)
                 for x in set(A).union(B)}.items():
        if k == 2:
            temp *= v
        else:
            temp *= v + 1
    cnt[n * (n - 1) // 2] = temp
    if temp > MAXN:
        # print(n*(n-1)//2, cnt[n*(n-1)//2])
        break
    n += 1

# print(len(cnt))
inv_cnt = {}
for k, v in cnt.items():
    inv_cnt[v] = min(inv_cnt.get(v, k), k)

inv_cnt = sorted(map(list, inv_cnt.items()))
# NOTE: find the smallest one
for i in range(len(inv_cnt) - 2, -1, -1):
    if inv_cnt[i][-1] > inv_cnt[i + 1][-1]:
        inv_cnt[i][-1] = inv_cnt[i + 1][-1]

#for k, v in inv_cnt:
#    print(k, v)
# print(len(inv_cnt))

T = int(input())

for t in range(T):
    N = int(input())

    def solve(N):
        # N <= 1000
        # t*(t+1)/2
        # gcd(t, t+1) = 1
        from bisect import bisect_right
        return inv_cnt[bisect_right(inv_cnt, [N, 1 << 31])][-1]

    print(solve(N))
