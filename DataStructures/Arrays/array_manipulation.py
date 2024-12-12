# https://www.hackerrank.com/challenges/crush/problem


import os


def arrayManipulation(n, queries):
    accumulated_sum = [0 for i in range(n + 2)]
    for a, b, k in queries:
        accumulated_sum[a] += k
        accumulated_sum[b + 1] -= k

    max_val = 0
    cur_val = 0
    for i in range(1, n + 1):
        cur_val += accumulated_sum[i]
        if cur_val > max_val:
            max_val = cur_val
    return max_val


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)

    fptr.write(str(result) + "\n")
    fptr.close()
