# https://www.hackerrank.com/challenges/connecting-towns/

T = int(input())
for t in range(T):
    N = int(input())
    import operator
    import functools
    print(functools.reduce(operator.mul, map(int, input().split()), 1))