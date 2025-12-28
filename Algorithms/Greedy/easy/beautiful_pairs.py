# https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true

import os
from collections import Counter


def beautifulPairs(A, B):
    count_a = Counter(A)
    count_b = Counter(B)

    ans = 0
    met = False
    for k in count_a:
        pairs = min(count_a[k], count_b.get(k, 0))
        ans += pairs
        if count_a[k] != count_b.get(k, 0):
            met = True

    if met:
        return ans + 1
    else:
        return ans - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
