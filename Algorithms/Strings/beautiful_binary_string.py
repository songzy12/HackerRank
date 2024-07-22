# https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true


def minSteps(n, B):
    # Complete this function
    i = 0
    count = 0
    while i + 3 <= len(B):  # index
        if B[i:i + 3] == '010':
            i += 2
            count += 1
        i += 1
    return count


n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)
