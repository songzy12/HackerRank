# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem?isFullScreen=true
#
# For the selected substring to be valid, we need the rest of the string satisfy the following condition:
#   For each of the char ATCG, its count can not be larger than n // 4.
# Thus, we can just enumerate the substrings. For each possible l, find the right most r.


def compute_prefix_sum(gene):
    prefix_sum = {c: [0 for i in range(len(gene))] for c in "ATCG"}
    for i in range(len(gene)):
        for c in "ATCG":
            prefix_sum[c][i] = (prefix_sum[c][i - 1] if i - 1 >= 0 else 0) + (
                1 if gene[i] == c else 0
            )
    return prefix_sum


def compute_suffix_sum(gene):
    suffix_sum = {c: [0 for i in range(len(gene))] for c in "ATCG"}
    for i in range(len(gene) - 1, -1, -1):
        for c in "ATCG":
            suffix_sum[c][i] = (suffix_sum[c][i + 1] if i + 1 < len(gene) else 0) + (
                1 if gene[i] == c else 0
            )
    return suffix_sum


def is_valid(gene, prefix_sum, suffix_sum, l, r):
    # compute the count of ATCG from [0, l-1] and [r+1, n-1]
    for c in "ATCG":
        count = (prefix_sum[c][l - 1] if l - 1 >= 0 else 0) + (
            suffix_sum[c][r + 1] if r + 1 < len(gene) else 0
        )
        if count > len(gene) // 4:
            return False
    return True


def find_left_most_r(gene, prefix_sum, suffix_sum, l, last_r):
    while not is_valid(gene, prefix_sum, suffix_sum, l, last_r):
        last_r += 1
    return last_r


def steadyGene(gene):
    prefix_sum = compute_prefix_sum(gene)
    suffix_sum = compute_suffix_sum(gene)

    l = 0
    last_r = -1
    res = len(gene)
    while l < len(gene):
        if not is_valid(gene, prefix_sum, suffix_sum, l, len(gene) - 1):
            break
        r = find_left_most_r(gene, prefix_sum, suffix_sum, l, last_r)
        cur_res = r - l + 1
        res = min(res, cur_res)
        last_r = r
        l += 1
    return res
