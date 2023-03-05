# https://www.hackerrank.com/challenges/summing-the-n-series/

T = int(input())
for t in range(T):
    n = int(input())
    print((n * n) % (1000000007))
