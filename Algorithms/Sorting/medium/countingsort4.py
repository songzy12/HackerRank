# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true

def countSort(arr):
    # Write your code here
    res = [[] for i in range(100)]

    for i, x in enumerate(arr):
        num, char = x
        if i < len(arr) // 2:
            char = '-'
        res[num].append(char)

    return res


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        num, char = input().rstrip().split()
        arr.append([int(num), char])

    res = countSort(arr)

    flat_res = []
    for t in res:
        if len(t) != 0:
            flat_res += t
    print(' '.join(flat_res))
