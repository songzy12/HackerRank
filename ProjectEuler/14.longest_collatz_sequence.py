# https://www.hackerrank.com/contests/projecteuler/challenges/euler014

maxn = 5000000

dp = [0 for i in range(maxn + 1)]
dp[1] = 1


def solve(n):
    if n > maxn:
        if n % 2 == 0:
            return solve(n // 2) + 1
        else:
            return solve(3 * n + 1) + 1

    if dp[n] != 0:
        return dp[n]
    if n % 2 == 0:
        dp[n] = solve(n // 2) + 1
    else:
        dp[n] = solve(3 * n + 1) + 1
    return dp[n]


for n in range(1, maxn + 1):
    solve(n)

ans = [0 for i in range(5000000 + 1)]
for n in range(2, maxn + 1):
    ans[n] = n
    if dp[n] < dp[n - 1]:
        dp[n] = dp[n - 1]
        ans[n] = ans[n - 1]

T = int(input())
for t in range(T):
    n = int(input())
    print(ans[n])
