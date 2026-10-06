# https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=false
#
# So we want to swap the largest ones to the front of the array, then what about
# the side effects during the swap? i.e., in one swap, we may actually put two
# elements to the intended positions at the same time.
# Another question is: besides swapping the largest element to the front, are
# there smarter strategies to get the same permutation using fewer swaps?
#
# Math: https://en.wikipedia.org/wiki/Permutation_group


import os


def largestPermutation(k, arr):
    index_map = {value: i for i, value in enumerate(arr)}

    swap_cnt = 0
    max_val = len(arr)
    for i in range(len(arr)):
        if swap_cnt == k:
            break

        if arr[i] == max_val:
            max_val -= 1
            continue

        # swap the current element with the max_val element
        max_val_index = index_map[max_val]
        index_map[arr[i]] = max_val_index
        arr[i], arr[max_val_index] = arr[max_val_index], arr[i]

        swap_cnt += 1
        max_val -= 1
    return arr


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
