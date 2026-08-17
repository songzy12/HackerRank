# https://www.hackerrank.com/challenges/equal/problem?isFullScreen=false
#
# Key insights:
# 1. Inverting the Operation (Relative Difference)
# 2. The Greedy Property for Coin Denominations $\{1, 2, 5\}$.
#   A canonical coin system is a set of coin denominations where the simple
#   greedy algorithm always finds the optimal (minimum) number of coins to make
#   any change amount. Most real-world national currencies, like the U.S. dollar
#   system [1, 5, 10, 25], are canonical.
# 3. Bounding the Target Baseline $T$

import os


def compute_ops_for_delta(delta):
    return (delta // 5) + ((delta % 5) // 2) + ((delta % 5) % 2)


def compute_ops_for_target(arr, target):
    total_ops = 0
    for x in arr:
        delta = x - target
        total_ops += compute_ops_for_delta(delta)
    return total_ops


def equal(arr):
    min_val = min(arr)
    ans = float("inf")

    candidate_targets = list(range(min_val - 4, min_val + 1))
    for target in candidate_targets:
        total_ops = compute_ops_for_target(arr, target)
        ans = min(ans, total_ops)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')
    fptr.close()
