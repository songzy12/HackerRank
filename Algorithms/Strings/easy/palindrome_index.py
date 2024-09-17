# https://www.hackerrank.com/challenges/palindrome-index?isFullScreen=true


def palindromeIndex(s):
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i >= j:
        # already a palindrome
        return -1

    # the answer can only be i0 or j0
    i0 = i
    j0 = j

    i += 1  # remove i0
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i >= j:
        return i0
    return j0
