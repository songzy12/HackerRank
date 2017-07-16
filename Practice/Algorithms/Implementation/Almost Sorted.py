n = int(raw_input())
nums = [int(x) for x in raw_input().split()]

def check(nums):
    for i, num in enumerate(nums):
        if not i:
            continue
        if num < nums[i-1]:
            return False
    return True

def index(nums):
    i1 = i2 = -1
    for i, num in enumerate(nums):
        if i + 1 < len(nums) and num > nums[i+1]:
            i1 = i
            break
        
    for i in range(len(nums)-1,-1,-1):
        if i > 0 and nums[i] < nums[i-1]:
            i2 = i
            break
    return i1, i2

def swap(nums, i1, i2):
    
    if i1 == -1 or i2 == -1:
        return False, -1, -1
    nums[i1], nums[i2] = nums[i2], nums[i1]
    if check(nums):
        return True, i1, i2
    nums[i1], nums[i2] = nums[i2], nums[i1]
    return False, i1, i2

def reverse(nums, i1, i2):    
    if i1 == -1 or i2 == -1:
        return False, -1, -1
    nums[i1:i2+1] = nums[i1:i2+1][::-1]
    if check(nums):
        return True, i1, i2
    nums[i1:i2+1] = nums[i1:i2+1][::-1]
    return False, i1, i2

def compute(nums):
    if check(nums):
        print 'yes'
        return

    i1, i2 = index(nums)
    
    f, l, r = swap(nums, i1, i2)
    if f:
        print 'yes'
        print 'swap', l+1, r+1
        return

    f, l, r = reverse(nums, i1, i2)
    if f:
        print 'yes'
        print 'reverse', l+1, r+1
        return

    print 'no'

compute(nums)
    
