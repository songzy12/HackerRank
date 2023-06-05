# https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem

import string


def dedup(key):
    s = set()
    ans = ''
    for k in key:
        if k not in s:
            ans += k
            s.add(k)
    return ans


def get_matrix(key):
    ans = [key]
    tmp = ''
    for i in string.ascii_uppercase:
        if i not in key:
            tmp += i
            if len(tmp) == len(key):
                ans.append(tmp)
                tmp = ''
    if len(tmp) != 0:
        ans.append(tmp)
    # print(ans)
    return ans


def rotate_matrix(matrix):
    ans = []
    for j in range(len(matrix[0])):
        column = ''
        for i in range(len(matrix)):
            if j < len(matrix[i]):
                column += matrix[i][j]
        ans.append(column)
    # print(ans)
    return ans


def transform(key):
    return ''.join(sorted(rotate_matrix(get_matrix(dedup(key)))))


def build_map(text):
    return {text[i]: string.ascii_uppercase[i] for i in range(26)}


def compute_original(massage, dict):
    dict[' '] = ' '
    return ''.join([dict[c] for c in message])


def decrypt(message, key):
    text = transform(key)
    # print(text, len(text))
    dict = build_map(text)
    # print(dict)
    return compute_original(message, dict)


N = int(input())
for _ in range(N):
    key = input()
    message = input()
    print(decrypt(message, key))
