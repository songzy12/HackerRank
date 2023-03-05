n = int(raw_input())
s = raw_input()

# note that the number of target chars in this substring
# may not be the same as the number we need to change,
# since we can keep several chars unchanged 

# be careful with python's variable scope

from collections import defaultdict

count = defaultdict(int)

limit = n / 4

def valid():
    for c in 'ATCG':
        if count[c] > limit:
            return False
    return True

def get_ans():
    # first we find the min possible t

    
    def get_t():
        # t + 1 ... n - 1 is valid
        # t ... n - 1 is not valid
        t = n - 1
        while t >= 0:
            count[s[t]] += 1
            if not valid():
                count[s[t]] -= 1
                return t
            t -= 1
        return t

    h = 0 # h can be larger

    def get_h(h, t):
        # we willl modify from h to t
        while h <= t:
            count[s[h]] += 1
            
            if not valid():
                count[s[h]] -= 1
                return h
            h += 1
        return h

    t = get_t() # t can only be larger
    
    ans = n
    while t < n:
        # find the largest h for now
        h = get_h(h, t)
        ans = min(ans, t - h + 1)        
        t += 1
        if t < n:
            count[s[t]] -= 1 # note the order
    return ans

print get_ans()
