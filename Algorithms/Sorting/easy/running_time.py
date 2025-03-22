# https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true

import os


def runningTime(arr):
    total_shift = 0
    for i in range(1, len(arr)):
        # In this loop, we will make arr[0...i] sorted.
        cur_num = arr[i]
        cur_shift = 0
        for j in range(i - 1, -1, -1):
            if arr[j] > cur_num:
                arr[j + 1] = arr[j]
                cur_shift += 1
            else:
                arr[j + 1] = cur_num
                break
        else:
            arr[j] = cur_num
        total_shift += cur_shift

        # print(i, arr)
    return total_shift


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + "\n")
    fptr.close()
