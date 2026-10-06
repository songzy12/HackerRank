# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

import os


def minimumAbsoluteDifference(arr):
    arr.sort()
    ans = abs(arr[1] - arr[0])
    for i in range(1, len(arr) - 1):
        ans = min(ans, abs(arr[i + 1] - arr[i]))
    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + "\n")
    fptr.close()
