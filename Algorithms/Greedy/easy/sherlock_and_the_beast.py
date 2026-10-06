# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?isFullScreen=true


def decentNumber(n):
    if n % 3 == 0:
        return "5" * n
    if n % 3 == 1 and n >= 10:
        return "5" * (n - 10) + "3" * 10
    if n % 3 == 2 and n >= 5:
        return "5" * (n - 5) + "3" * 5
    return "-1"


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
