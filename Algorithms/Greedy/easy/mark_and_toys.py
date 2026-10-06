# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true


import os


def maximumToys(prices, k):
    prices.sort()

    total = 0
    count = 0
    for price in prices:
        if total + price > k:
            break
        total += price
        count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + "\n")
    fptr.close()
