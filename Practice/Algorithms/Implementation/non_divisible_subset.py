from collections import defaultdict, Counter

n, k = [int(x) for x in raw_input().split()]
nums = Counter([int(x) % k for x in raw_input().split()])

m = defaultdict(int)
for num in nums:
    if (2 * num) % k == 0:  # do not forget this
        m[num] = 1

    if num not in m and k - num not in m:
        m[num] = max(nums[num], nums[k - num])
print sum(m.values())
