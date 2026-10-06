# https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true
#
# Generalization: max matching, bipartite graph, Hungarian algorithm, etc.
# But for this specific problem, a simple greedy approach suffices.

import os
from collections import Counter


def beautifulPairs(A, B):
    count_a = Counter(A)
    count_b = Counter(B)

    ans = 0
    for k in set(count_a.keys()) | set(count_b.keys()):
        ans += min(count_a[k], count_b.get(k, 0))

    if ans == len(A):
        return ans - 1
    return ans + 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + "\n")
    fptr.close()
