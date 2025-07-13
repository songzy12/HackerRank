# https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

import os


def pairs(k, arr):
    set_arr = set(arr)

    ans = 0
    for a in arr:
        if a + k in set_arr:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
