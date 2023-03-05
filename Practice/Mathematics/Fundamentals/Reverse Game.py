# https://www.hackerrank.com/challenges/reverse-game

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    # the final position would be n - 1, 0, n - 2, 1, ...
    head = K
    tail = N - 1 - K
    if head < tail:  # note the order
        print(2 * head + 1)
    else:
        print(2 * tail)
