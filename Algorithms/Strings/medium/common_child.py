# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true
#
# This is actually the classical longest common subsequence problem:
# https://en.wikipedia.org/wiki/Longest_common_subsequence


def commonChild(s1, s2):
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        dp[i][0] = 0
    for j in range(len(s2) + 1):
        dp[0][j] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(commonChild(s1, s2))
