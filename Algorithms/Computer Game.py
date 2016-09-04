import sys

stdin, stdout = sys.stdin, sys.stdout
fin = open('in_.txt', 'r')
# fout = open('out_.txt', 'w')
sys.stdin = fin
# sys.stdout = fout

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

edgeA = {} # key: nodes in A
edgeB = {} # key: nodes in B

'''def gcd(x, y):
    while y:
        x, y = y, x % y
    return x'''

from fractions import gcd

for i in range(n):
    edgeA[i] = []
for i in range(n):
    edgeB[i] = []
for i in range(n):
    for j in range(n):
        if gcd(A[i],B[j]) == 1:
            continue
        edgeA[i].append(j)
        edgeB[j].append(i)

#print(A, B)
#print(edgeA)
#print(edgeB)

# visited = [False for i in range(n)]
matchA = [n for i in range(n)] # key: nodes in A, n for nil
matchB = [n for j in range(n)] # key: nodes in B
matching = 0
dist = [1<<20 for i in range(n+1)] # dist[n] = nil

def BFS():
    Q = []
    for u in range(n):
        if matchA[u] == n:
            dist[u] = 0
            Q += [u]
        else:
            dist[u] = 1<<20
    dist[n] = 1<<20
    while len(Q): # while Q not empty
        u = Q.pop(0)
        if dist[u] < dist[n]:
            for v in edgeA[u]:
                if dist[matchB[v]] == 1<<20:
                    dist[matchB[v]] = dist[u] + 1
                    Q += [matchB[v]]
    return True if dist[n]!=(1<<20) else False

def DFS(u):
    if u != n:
        for v in edgeA[u]:
            if dist[matchB[v]] == dist[u] + 1:
                if DFS(matchB[v]):
                    matchB[v], matchA[u] = u, v
                    return True
        dist[u] = 1<<20
        return False
    return True

while BFS():
    # BFS decides whether to continue
    for u in range(n):
        if matchA[u] == n:
            if DFS(u):
                matching += 1

##def path(a):
##    for b in edgeA[a]:
##        if visited[b]:
##            continue
##        visited[b] = True
##        if matchB[b] == n or path(matchB[b]):
##            matchA[a], matchB[b] = b, a
##            return 1
##    return 0
##
##for i in range(n):
##    if matchA[i] == n:
##        visited = [False for i in range(n)]
##        matching += path(i)

print(matching)

fin.close()
# fout.close()
sys.stdin, sys.stdout = stdin, stdout
