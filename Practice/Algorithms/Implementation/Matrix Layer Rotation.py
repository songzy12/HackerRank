import sys
fin = open('in.txt', 'r')
fout = open('out.txt', 'w')
stdin, stdout = sys.stdin, sys.stdout
sys.stdin, sys.stdout = fin, fout

M, N, R = map(lambda x: int(x), input().split())
A = [[] for row in range(M)]
for row in range(M):
    A[row] = list(map(lambda x: int(x), input().split()))

def rotate(i, j, R, l, r, t, b):
    if i == t and j > l:
        seg = j - l
        return (i, j-R) if R <= seg else rotate(t, l, R-seg, l, r, t, b)
    elif i == b and j < r:
        seg = r - j
        return (i, j+R) if R <= seg else rotate(b, r, R-seg, l, r, t, b)
    elif j == l and i < b:
        seg = b - i
        return (i+R, j) if R <= seg else rotate(b, l, R-seg, l, r, t, b)
    elif j == r and i > t:
        seg = i - t
        return (i-R, j) if R <= seg else rotate(t, r, R-seg, l, r, t, b)
    
m = {}
inv = {}
for i in range(M):
    for j in range(N):
        layer = min(i, j, M-1-i, N-1-j)
        l, r, t, b = layer, N-1-layer, layer, M-1-layer
        total = 2*((M-2*layer)+(N-2*layer))-4
        # print('(%d, %d), (%d, %d, %d, %d) %d %d' % (i, j, l, r, t, b, layer, total))
        m[(i,j)] = rotate(i, j, R%total, l, r, t, b)
# B = [[0 for j in range(N)] for i in range(M)]
# print(len(m), m)
for i in range(M):
    for j in range(N):
        inv[m[(i,j)]] = (i,j)
        # print(m[(i,j)], i0, j0)
        # B[i][j] = A[i0][j0]
# print(m)
# print(inv)
for i in range(M):
    for j in range(N):
        i0, j0 = inv[(i,j)]
        print(A[i0][j0], end = " ")
        pass
    print()
    
fout.close()
fin.close()
sys.stdin, sys.stdout = stdin, stdout
