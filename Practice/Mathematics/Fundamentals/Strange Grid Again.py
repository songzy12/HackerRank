# https://www.hackerrank.com/challenges/strange-grid/problem

r, c = map(int, input().split())

if r % 2 == 1:
    print(r // 2 * 10 + 2 * c - 2)
else:
    print((r - 1) // 2 * 10 + 2 * c - 1)  # remember to -1
