# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    num = input()

    def solve(num, n, k):
        ans = 0
        head = tail = 0
        cur_prod = 1
        while tail < n:
            cur_num = int(num[tail])
            # print(head, tail, cur_num, cur_prod)
            if cur_num == 0:
                cur_prod = 1
                head = tail + 1  # NOTE: care for the order and modification
            elif tail - head + 1 < k:
                cur_prod *= cur_num
            else:
                cur_prod *= cur_num
                if cur_prod > ans:
                    ans = cur_prod
                cur_prod //= int(num[head])
                head += 1
            tail += 1
        return ans

    print(solve(num, n, k))
