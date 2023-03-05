# https://www.hackerrank.com/challenges/special-multiple/


def solve(N):
    n = 1
    while True:
        temp = int(bin(n)[2:].replace('1', '9'))
        if temp % N == 0:
            return temp
        n += 1


T = int(input())
for t in range(T):
    N = int(input())
    print(solve(N))
