# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true


def minimumNumber(unused, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    def needsOne(password, charset):
        for t in password:
            if t in charset:
                return 0
        return 1

    res = (
        needsOne(password, numbers)
        + needsOne(password, lower_case)
        + needsOne(password, upper_case)
        + needsOne(password, special_characters)
    )
    return max(res, 6 - len(password))
