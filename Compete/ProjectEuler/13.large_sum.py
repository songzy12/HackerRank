# https://www.hackerrank.com/contests/projecteuler/challenges/euler013

N = int(input())
nums = []
for n in range(N):
    nums.append(input())

length = 50

ans = []
cur = 0
carry = 0
for i in range(length - 1, -1, -1):
    cur = carry
    for j in range(N):
        cur += int(nums[j][i])
    # print(cur)
    carry = cur // 10
    cur %= 10
    ans.append(cur)

# NOTE: here carry may be larger than 9
while carry:
    ans.append(carry % 10)
    carry //= 10

print(''.join(map(str, ans[-10:][::-1])))
