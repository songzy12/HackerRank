# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true


def richieRich(s, n, k):
    i = 0
    j = len(s) - 1
    s = list(s)

    changed = [False for t in range(n)]  # stupid
    num_changed = 0
    while i < j:
        if s[i] != s[j]:
            if num_changed == k:
                break
            num_changed += 1
            changed[i] = True
            if s[i] > s[j]:
                s[j] = s[i]
            else:
                s[i] = s[j]
        i += 1
        j -= 1
    if i < j:
        return -1

    i = 0
    j = len(s) - 1
    while i < j and num_changed < k:
        if s[i] != '9':
            if not changed[i] and num_changed + 2 <= k:
                s[i] = '9'
                s[j] = '9'
                num_changed += 2
            if changed[i] and num_changed + 1 <= k:
                s[i] = '9'
                s[j] = '9'
                num_changed += 1
        i += 1
        j -= 1

    if i == j and num_changed < k:
        s[i] = '9'
    return ''.join(s)


n, k = [int(t) for t in raw_input().split()]
s = raw_input().strip()
result = richieRich(s, n, k)
print(result)
