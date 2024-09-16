# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true
#
# Just enumerate all the possible lengths.


def compute_pairs_of_length(s, l):
    ans = 0

    m = {}
    cur = [0 for i in range(26)]
    for i in range(l):
        cur[ord(s[i]) - ord("a")] += 1
    m[tuple(cur)] = 1

    for i in range(l, len(s)):
        cur[ord(s[i - l]) - ord("a")] -= 1
        cur[ord(s[i]) - ord("a")] += 1
        if tuple(cur) in m:
            ans += m[tuple(cur)]
            m[tuple(cur)] += 1
        else:
            m[tuple(cur)] = 1
    return ans


def sherlockAndAnagrams(s):
    ans = 0
    for l in range(1, len(s)):
        ans += compute_pairs_of_length(s, l)
    return ans
