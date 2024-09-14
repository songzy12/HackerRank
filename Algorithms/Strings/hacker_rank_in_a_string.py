# https://www.hackerrank.com/challenges/hackerrank-in-a-string?isFullScreen=true


def hackerrankInString(s):
    p = "hackerrank"

    i = 0
    j = 0
    while i < len(p):
        while j < len(s) and s[j] != p[i]:
            j += 1
        if j == len(s):
            break
        i += 1
        j += 1

    return "YES" if i == len(p) else "NO"
