# https://www.hackerrank.com/challenges/maximum-palindromes/problem?isFullScreen=true
#
# Two steps:
# 1. For give l and r, compute a map of each char to its count.
# 2. Then, for such a map, compute the number of palindromes.
#    a. We count the possiblities that the chars can be put in the middle and on both sides.
#    b. For each key k, with count c[k]
#       i.  if c[k] // 2 > 0, then c[k] // 2 can be put symmetrically on both sides
#       ii. if c[k] % 2 === 1, then this char can also be put in the middle
#    c. To construct a maximum palindorme, there are 2 steps:
#       i. pick one from the chars that can be put in the middle
#       ii. choose a combination of the chars that can be put on the sides
#       So the answer would be len(char_mid) * combination(char_sides)
#       Here combination(char_sides) = (\sum char_sides[i])! / \prod (char_sides[i])!
# 3. To compute the module, one can use Fermat's Little Theorem, a.k.a, a^{-1} = a^{p-2} (mod p)
#
# References: 
# 1. https://en.wikipedia.org/wiki/Prefix_sum
# 2. https://en.wikipedia.org/wiki/Binomial_coefficient#Generalization_to_multinomials
# 3. https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
# 4. https://en.wikipedia.org/wiki/Exponentiation_by_squaring

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
    tmp = compute_pow(i, p // 2) ** 2 % MOD
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


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()
    initialize(s)

    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + "\n")

    fptr.close()
