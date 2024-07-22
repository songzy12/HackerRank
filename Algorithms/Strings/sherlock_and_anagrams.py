# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true


def sherlockAndAnagrams(s):
    ans = 0
    from collections import defaultdict
    for step in range(1, len(s)):

        m = defaultdict(int)
        cur = [0 for i in range(26)]
        for i in range(step):
            cur[ord(s[i]) - ord('a')] += 1
        m[tuple(cur)] = 1
        for i in range(step, len(s)):
            cur[ord(s[i - step]) - ord('a')] -= 1
            cur[ord(s[i]) - ord('a')] += 1
            if m[tuple(cur)]:
                ans += m[tuple(cur)]
            m[tuple(cur)] += 1
    return ans


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = sherlockAndAnagrams(s)
    print(result)

# enumerate the possible length
