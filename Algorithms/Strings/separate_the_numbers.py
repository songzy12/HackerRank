# https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true


def check(s, num):
    i = 0
    while i < len(s):
        l = len(str(num))
        if s[i:i + l] != str(num):
            return False
        num += 1
        i += l
    return i == len(s)


def check_(s):
    for i in range(1, len(s) / 2 + 1):  # notice the index
        if check(s, int(s[:i])):
            return 'YES', s[:i]
    return 'NO', ''


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    print(' '.join(check_(s)))
