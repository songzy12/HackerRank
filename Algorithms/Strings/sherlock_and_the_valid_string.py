# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true
#
# We can first count the number of each char. Then:
# 1. if all chars appear for the same time, then the string is valid
# 2. if not, since we can only remove one char, which means we can only decrease the count of one char by 1, 
#    so we require there are at most two different counts:
#    a. we decrease the large one and the string becomes valid. The large count is 1 larger than the small count.
#    b. we decrease the small one and the string becomes valid. The small count is 1.

from collections import Counter


def isValid(s):
    count_by_char = Counter(s)
    count_by_count = Counter(count_by_char.values())
    if len(count_by_count) == 1:
        return "YES"
    if len(count_by_count) > 2:
        return "NO"
    small_count, large_count = sorted(count_by_count.keys())
    if large_count - small_count == 1 and count_by_count[large_count] == 1:
        return "YES"
    if small_count == 1 and count_by_count[small_count] == 1:  # another case
        return "YES"
    return "NO"
