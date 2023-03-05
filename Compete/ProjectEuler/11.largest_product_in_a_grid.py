# https://www.hackerrank.com/contests/projecteuler/challenges/euler011

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)


def solve_line(nums):
    #print(nums)
    head = 0
    tail = 0
    ans = 0
    cur_prod = 1
    while tail < len(nums):
        if nums[tail] == 0:
            head = tail + 1
            cur_prod = 1
        elif tail - head + 1 < 4:
            cur_prod *= nums[tail]
        else:
            cur_prod *= nums[tail]

            # print(head, tail, cur_prod, ans)
            if cur_prod > ans:
                ans = cur_prod
            cur_prod //= nums[head]
            head += 1
        tail += 1
    return ans


def solve():
    ans = 0
    for line in grid:
        temp = solve_line(line)
        ans = max(ans, temp)

    for line in [[grid[i][j] for i in range(20)] for j in range(20)]:
        temp = solve_line(line)
        ans = max(ans, temp)

    for i in range(20):
        line = []
        k = 0
        while i + k < 20 and k < 20:
            line.append(grid[i + k][k])
            k += 1
        temp = solve_line(line)
        ans = max(ans, temp)

    for j in range(1, 20):
        line = []
        k = 0
        while k < 20 and j + k < 20:
            line.append(grid[k][j + k])
            k += 1
        temp = solve_line(line)
        ans = max(ans, temp)

    # NOTE: another diagonal direction

    for i in range(20):
        line = []
        k = 0
        while i - k >= 0 and k < 20:
            line.append(grid[i - k][k])
            k += 1
        temp = solve_line(line)
        ans = max(ans, temp)

    for j in range(1, 20):
        line = []
        k = 0
        while 19 - k >= 0 and j + k < 20:
            line.append(
                grid[19 -
                     k][j +
                        k])  # NOTE: here is how to compute the diagonal line
            k += 1
        temp = solve_line(line)
        ans = max(ans, temp)

    return ans


print(solve())
