# https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true


def check(s, num):
    i = 0
    while i < len(s):
        l = len(str(num))
        if s[i : i + l] != str(num):
            return False
        num += 1
        i += l
    return i == len(s)


def separateNumbers(s):
    # so we just enumerate all possible splits.
    for i in range(1, len(s) // 2 + 1):
        if check(s, int(s[:i])):
            print("YES", s[:i])
            return
    print("NO")
