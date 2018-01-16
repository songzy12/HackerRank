# https://www.hackerrank.com/contests/projecteuler/challenges/euler009

# b = (N*N-2*N*a) / (2*N-2*a)
# c = N - (a+b)

T = int(input())
for t in range(T):
    N = int(input())
    def solve(N):
        ans = -1
        for a in range(1, N):
            top = (N*N-2*N*a)
            bottom = (2*N-2*a)
            if top % bottom != 0:
                continue
            b = top // bottom
            if b <= 0:
                continue
            c = N - a - b
            if c <= 0:
                continue
            
            if a * b * c > ans:
                ans = a * b * c
        return ans
    print(solve(N))
