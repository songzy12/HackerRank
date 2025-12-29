# https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true

import os


def jimOrders(orders):
    mapped_orders = []
    for order_id, order in enumerate(orders):
        mapped_orders.append((order[0] + order[1], order_id))
    mapped_orders.sort()
    return [order_id + 1 for _, order_id in mapped_orders]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
