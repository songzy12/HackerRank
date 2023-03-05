n = int(input())
nums = []
for i in range(n):
    nums.append(input())


from functools import cmp_to_key

def cmp(a, b):
    if len(a) != len(b):
        return len(a) - len(b) 
    for i in range(len(a)):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i]) # ord
    return 0

nums.sort(key=cmp_to_key(cmp)) # cmp_to_key
for i in nums:
    print (i)
