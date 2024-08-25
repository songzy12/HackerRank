# https://www.hackerrank.com/challenges/maximum-palindromes/problem?isFullScreen=true
#
# Two steps:
# 1. For give l and r, compute a map with 26 keys, from each letter to its count.
# 2. Then, for such a map, compute the number of palindromes.
#    a. init array_even[] and count_mid
#    b. first, for each key k, with count c[k]
#       i.  if c[k] // 2 > 0, array_even.append(c[k] // 2)
#       ii. if c[k] % 2 === 1, count_mid += 1
#    c. the answer would be count_mid * combination(array_even)
#       i. here combination(array_even) = (\sum array_even[i])! / \prod (array_even[i])!

import os
import string

MAX_LEN = int(1e5) + 1
MOD = int(1e9) + 7

prefix_sum = [[0 for i in range(26)] for j in range(MAX_LEN)]
factors = [1 for i in range(MAX_LEN)]
inv_n = [1 for i in range(MAX_LEN)]
inv_factors = [1 for i in range(MAX_LEN)]


def compute_pow(i, p):
    if p == 0:
        return 1
    tmp = compute_pow(i, p // 2)**2 % MOD
    if p % 2 == 0:
        return tmp
    return tmp * i % MOD


def initialize(s):
    lowercases = string.ascii_lowercase

    for i in range(1, len(s) + 1):
        for j in range(26):
            prefix_sum[i][j] = prefix_sum[i - 1][j]
        prefix_sum[i][lowercases.index(s[i - 1])] += 1

    for i in range(1, MAX_LEN):
        inv_n[i] = compute_pow(i, MOD - 2)

    for i in range(1, MAX_LEN):
        factors[i] = factors[i - 1] * i % MOD

    for i in range(1, MAX_LEN):
        inv_factors[i] = inv_factors[i - 1] * inv_n[i] % MOD


def combinator(side_counts):
    result = factors[sum(side_counts)]
    for side_count in side_counts:
        result *= inv_factors[side_count]
        result %= MOD
    return result


def compute(mid_count, side_counts):
    result = combinator(side_counts)
    if mid_count > 0:
        return mid_count * result % MOD
    return result


def answerQuery(l, r):
    # Suppose prefix_sum[l][26] to be the number of counts from 1 to l.
    count = [0 for i in range(26)]
    for i in range(26):
        count[i] = prefix_sum[r][i] - prefix_sum[l - 1][i]

    mid_count = 0
    side_counts = []
    for i in range(26):
        mid_count += count[i] % 2
        if count[i] // 2 > 0:
            side_counts.append(count[i] // 2)
    return compute(mid_count, side_counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
