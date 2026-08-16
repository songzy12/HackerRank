# https://www.hackerrank.com/challenges/maxsubarray/problem
#
# We define subsequence as any subset of an array.
# We define a subarray as a contiguous subsequence in an array.
#
# Given an array, find the maximum possible sum among:
# 1. all nonempty subarrays.
# 2. all nonempty subsequences.
#
# https://en.wikipedia.org/wiki/Maximum_subarray_problem

import os


def compute_max_subarray(arr):
    """
    DP: for arr[1...i], we need to maintain two things: 
    1. max_sum[i]: the maximum subarray sum ending at index i
    2. max_sum_so_far: the maximum subarray sum found so far

    Then, with one more element arr[i+1], we can compute max_sum[i+1] as:
        max_sum[i+1] = max(arr[i+1], arr[i+1] + max_sum[i])
    and update max_sum_so_far as:
        max_sum_so_far = max(max_sum_so_far, max_sum[i+1])
    """
    max_sum = arr[0]
    max_sum_so_far = arr[0]
    for i in range(1, len(arr)):
        max_sum = max(arr[i], arr[i] + max_sum)
        max_sum_so_far = max(max_sum_so_far, max_sum)
    return max_sum_so_far


def compute_max_subsequence(arr):
    """
    Trivial: The maximum subsequence sum is the sum of all positive numbers in
    the array. If all numbers are negative, then the maximum subsequence sum is
    the largest (least negative) number in the array.
    """
    max_sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            max_sum += arr[i]

    if max_sum > 0:
        return max_sum
    else:
        return max(arr)


def solve(arr):
    return compute_max_subarray(arr), compute_max_subsequence(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = solve(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
