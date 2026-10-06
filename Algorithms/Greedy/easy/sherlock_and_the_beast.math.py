# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=true
#
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
#
# let 3 n_1 be the number of 5's and 5 n_2 be the number of 3's
# 3 n_1 + 5 n_2 = n
#
# n_1 = 2n - 5k
# n_2 = -n + 3k
# here k \in [ceil(n/3), floor(2n/5)]
#
# max n_1, then k = ceil(n/3)
#
# n_2 = -n + 3 * ceil(n/3)
# n_1 = 2n - 5 * ceil(n/3)
#
# number of 5s: 3 n_1 = 3 * (2n - 5 * ceil(n/3))
# number of 3s: 5 n_2 = 5 * (-n + 3 * ceil(n/3))

import math


def decentNumber(n):
    n_5 = 3 * (2 * n - 5 * math.ceil(n / 3))
    n_3 = 5 * (-n + 3 * math.ceil(n / 3))

    if n_5 < 0 or n_3 < 0:
        return "-1"
    return "5" * n_5 + "3" * n_3


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
