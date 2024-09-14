# https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true

import string


def compute_weights(s):
    weights_map = {c: ord(c) - ord("a") + 1 for c in string.ascii_lowercase}

    weights = set()
    i = 0
    last_char = ""
    cur_length = 1
    while i < len(s):
        if i == 0 or s[i] != s[i - 1]:
            last_char = s[i]
            cur_length = 1
        else:
            cur_length += 1
        weights.add(weights_map[s[i]] * cur_length)
        i += 1

    return weights


def weightedUniformStrings(s, queries):
    weights = compute_weights(s)
    results = []
    for query in queries:
        if query in weights:
            results.append("Yes")
        else:
            results.append("No")
    return results
