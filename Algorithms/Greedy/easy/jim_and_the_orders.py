# https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true

import os


def jimOrders(orders):
    mapped_orders = []
    for index, [order_time, prep_time] in enumerate(orders):
        mapped_orders.append((order_time + prep_time, index + 1))
    mapped_orders.sort()
    return [order_id for _, order_id in mapped_orders]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
