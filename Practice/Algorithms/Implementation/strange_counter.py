t = int(raw_input())
import math
def get_k_left(n):
    k = int(math.log(n / 3.0 + 1, 2))
    return k, n - 3*(2**k-1)
    
    
k, left = get_k_left(t)

if not left:
    print 1
else:
    print 3*2**k-left+1

