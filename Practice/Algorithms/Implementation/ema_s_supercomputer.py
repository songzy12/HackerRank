# brute force

n, m = [int(x) for x in raw_input().split()]
grid = []

for i in range(n):
    grid.append(raw_input())


def compute_t(i, j):
    t = 0

    def valid(i, j):
        return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 'G'

    while valid(i - t, j) and valid(i + t, j) and valid(i, j - t) and valid(
            i, j + t):
        t += 1
    return t - 1


def compute_area(t):
    return 4 * t + 1


ts = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(compute_t(i, j))
    ts.append(temp)


def touch(i0, j0, t0, i1, j1, t1):
    if t0 == -1 or t1 == -1:
        return True
    if i0 == i1:
        return i0 + t0 >= i1 - t1
    if j0 > j1:
        return j0 - t0 <= j1 and i1 - t1 <= i0 or\
               i0 + t0 >= i1 and j1 + t1 >= j0
    if j0 == j1:
        return j0 - t0 <= j1 + t1
    if j0 < j1:
        return j0 + t0 >= j1 and i1 - t1 <= i0 or \
               i0 + t0 >= i1 and j1 - t1 <= j0


def compute_area(i0, j0, i1, j1):
    T0 = ts[i0][j0]
    T1 = ts[i1][j1]

    temp = [0]
    for t0 in range(T0, -1, -1):
        t1 = T1
        while t1 >= 0 and touch(i0, j0, t0, i1, j1, t1):
            t1 -= 1
        if t1 != -1:
            temp.append((4 * t0 + 1) * (4 * t1 + 1))
    return max(temp)


# cannot overlap
# when check position i0, j0 and i1, j1.
# the corresponding t may not be ts[i0][j0]
# for example,

ans = 0
for i0 in range(n):
    for j0 in range(m):
        i1 = i0
        for j1 in range(j0 + 1, m):
            temp = compute_area(i0, j0, i1, j1)
            ans = max(temp, ans)
        for i1 in range(i0 + 1, n):
            for j1 in range(m):
                temp = compute_area(i0, j0, i1, j1)
                ans = max(temp, ans)
print ans
