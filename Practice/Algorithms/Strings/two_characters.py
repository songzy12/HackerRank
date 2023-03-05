def char2index(c):
    return ord(c) - ord('a')


num = 26

chars = [['' for i in range(num)] for j in range(num)]
counts = [[0 for i in range(num)] for j in range(num)]
# in python, not chars = [['']*num]*num

n = int(raw_input())
s = raw_input()

for c in s:
    i = char2index(c)

    for row in range(26):
        if not chars[row][i]:
            chars[row][i] = c
            counts[row][i] = 1
        elif chars[row][i] == c or counts[row][i] == -1:
            counts[row][i] = -1
        else:
            chars[row][i] = c
            counts[row][i] += 1

    for col in range(26):
        if not chars[i][col]:
            chars[i][col] = c
            counts[i][col] = 1
        elif chars[i][col] == c or counts[i][col] == -1:
            counts[i][col] = -1  # stupid
        else:
            chars[i][col] = c
            counts[i][col] += 1

ans = max([max(row) for row in counts])
# alternating
print ans if ans > 1 else 0
