# https://www.hackerrank.com/challenges/sherlock-and-cost/problem?isFullScreen=false
#
# Optimality Principle: For any optimal array $A$, every element $A[i]$ can be
# chosen as either the minimum possible value ($1$) or the maximum possible
# value ($B[i]$). Intermediate values ($1 < A[i] < B[i]$) are never strictly
# necessary to achieve the maximum sum.
#
#
# DP: define two arrays, low and high, where:
#   low[i] = maximum cost of A[1..i] if A[i] is 1
#   high[i] = maximum cost of A[1..i] if A[i] is B[i]
# Then we have:
#   low[i] = max(low[i-1], high[i-1] + abs(1 - B[i-1]))
#   high[i] = max(low[i-1] + abs(B[i] - 1), high[i-1] + abs(B[i] - B[i-1]))
# And the answer is max(low[n], high[n]).
import os


def cost(B):
    low = 0
    high = 0

    n = len(B)
    for i in range(1, n):
        low_new = max(low, high + abs(1 - B[i - 1]))
        high_new = max(low + abs(B[i] - 1), high + abs(B[i] - B[i - 1]))
        low, high = low_new, high_new
    return max(low, high)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')
    fptr.close()
