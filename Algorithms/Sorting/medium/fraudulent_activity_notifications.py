# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
#
# Data stream, find the medium of the last k elements efficiently.
#
# Note the input range in [0, 200], so we can use count sort.

import os

def compute_median_x2(counts, d):
    count = 0
    median1 = None
    median2 = None

    if d % 2 == 1:
        mid = d // 2 + 1
        for num, cur_count in enumerate(counts):
            count += cur_count
            if count >= mid:
                return num * 2
    else:
        mid1 = d // 2
        mid2 = mid1 + 1
        for num, cur_count in enumerate(counts):
            count += cur_count
            if median1 is None and count >= mid1:
                median1 = num
            if count >= mid2:
                median2 = num
                break
        return median1 + median2


def should_alert(median_x2, num):
    if num >= median_x2:
        return True
    return False


def activityNotifications(expenditure, d):
    counts = [0] * 201
    alerts = 0

    for i in range(d):
        counts[expenditure[i]] += 1
    
    for i in range(d, len(expenditure)):
        median_x2 = compute_median_x2(counts, d)

        if should_alert(median_x2, expenditure[i]):
            alerts += 1
        # Remove the oldest element
        old_value = expenditure[i - d]
        counts[old_value] -= 1
        # Add the new element
        new_value = expenditure[i]
        counts[new_value] += 1
    return alerts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
