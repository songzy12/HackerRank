# https://www.hackerrank.com/contests/projecteuler/challenges/euler010

T = int(input().strip())

primes = [(2, 2)]  # put all this outside the for loop
t = 3

from math import sqrt

for a0 in range(T):
    n = int(input().strip())

    def check(t):
        for i in primes:
            if i[0] > sqrt(t):
                return True
            if t % i[0] == 0:
                return False

    while primes[-1][0] < n:
        if check(t):
            primes.append((t, primes[-1][-1] + t))
        t += 2

    def solve(n):
        import bisect
        index = bisect.bisect(
            primes,
            (n,
             1 << 64))  # NOTE: here the second number needs to be very large
        # print(primes, index)
        return primes[index - 1][-1]

    print(solve(n))
