# https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true


def beautifulBinaryString(b):
    count = 0

    i = 0
    while i + 3 <= len(b):
        if b[i : i + 3] == "010":
            # If there is a substring of 010, we can just change it to 011.
            i += 3
            count += 1
        else:
            i += 1
    return count
