# https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=false
#
# Let dp[index][amount] represents the number of ways to make change for
# 'amount' using the first 'index' coins.
# Then we have:
#   dp[index][amount] = \sum_{k} dp[index - 1][amount - k*c[index]] for all k
#   such that amount - k*c[index] >= 0
#
# However, note that we can also write:
#   dp[index][amount] = dp[index - 1][amount] + dp[index][amount - c[index - 1]]

import os


def getWays(n, c):
    """Calculate the number of ways to make change for a given amount.

    Args:
        n (int): The amount to make change for.
        c (list of int): The available coin values.

    Returns:
        int: The number of ways to make the change.
    """
    dp = [[0] * (n + 1) for _ in range(len(c) + 1)]
    dp[0][0] = 1
    for i in range(1, len(c) + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j] + (dp[i][j - c[i - 1]] if j >= c[i - 1] else 0)
    return dp[len(c)][n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')
    fptr.close()
