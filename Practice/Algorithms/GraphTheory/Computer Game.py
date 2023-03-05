# There are two random arrays A & B, each having the same number of elements. 
# The game begins with Sophia removing a pair (Ai, Bj) from the array if they are not co-prime.
# Sophia wants to find out the maximal number of times(S) she can do this on the arrays.

from math import sqrt
import sys
stdin = sys.stdin
sys.stdin = open('in_.txt', 'r')

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#print(A, B)

def calcSieve(maxValue):
    isPrime = [True for i in range(maxValue)]
    isPrime[0] = isPrime[1] = False
    L = int(sqrt(maxValue))
    for i in range(2, L + 1):
        if isPrime[i]:
            for j in range(i*i, maxValue, i):
                # start from i*i, (i-1)*i is False since i-1
                isPrime[j] = False
    return isPrime

def compressSieve(isPrime):
    primes = []
    end = len(isPrime)
    for i in range(2, end):
        if isPrime[i]:
            primes += [i]
    return primes

primeIds = {} # all use 0, 1, 2 ...
def getPrimeId(prime):
    if prime not in primeIds:
        primeIds[prime] = len(primeIds)
    return primeIds[prime]

matchL = matchR = visitedL = visitedR = primeIdsA = bMatchList = None

def match(u, visitedI):
    global visitedL, matchL, matchR, visitedR

    if visitedL[u] == visitedI:
    # on which level u is visited
        return False
    
    visitedL[u] = visitedI
    factors = primeIdsA[u]
    # first try to match the unmatched 
    for i in range(len(factors)):
        if visitedR[factors[i]] == visitedI:
            continue
        for j in range(len(bMatchList[factors[i]])):
            v = bMatchList[factors[i]][j]
            if matchR[v] < 0:
                matchL[u], matchR[v] = v, u
                return True
    # then begin to recurse
    for i in range(len(factors)):
        if visitedR[factors[i]] == visitedI:
            continue
        visitedR[factors[i]] = visitedI
        for j in range(len(bMatchList[factors[i]])):
            v = bMatchList[factors[i]][j]
            if matchL[u] != v and match(matchR[v], visitedI):
                matchL[u], matchR[v] = v, u
                return True
    return False

# we add one layer of primes between the two layers of numbers
# thus reduce the number of edges
# do not use match, use maximum flow.
def getMaximumRemovals(a, b):
    MAX = 10**9
    isPrime = calcSieve(int(sqrt(MAX)))
    primes = compressSieve(isPrime)
    # middle layer reduces number of edges
    # DINIC algorithm for network flow
    global primeIdsA, bMatchList, matchL, matchR, visitedL, visitedR
    primeIdsA = [[] for i in range(len(B))]
    for i in range(len(a)):
        primeFactors = [] # just for A
        x = a[i]
        for j in range(len(primes)):
            if primes[j] * primes[j] > x:
                break
            if x % primes[j] == 0:
                primeFactors += [primes[j]]
            while x % primes[j] == 0:
                x //= primes[j]
        if x > 1:
            primeFactors += [x]
            # that's why we only need sqrt(n)
            # the second largest prime <= sqrt(n)
    
        end = len(primeFactors)
        for j in range(end):
            primeIdsA[i] += [getPrimeId(primeFactors[j])]
    # print(A, primeIds, B)
    # print(primeIdsA)

    bMatchList = [[] for j in range(len(primeIds))] # TODO
    for i in range(len(b)):
        x = b[i]
        for j in range(len(primes)):
            if primes[j] * primes[j] > x:
                break
            if x % primes[j] == 0 and primes[j] in primeIds:
                bMatchList[primeIds[primes[j]]] += [i]
            while x % primes[j] == 0:
                x //= primes[j]
        
        if x > 1 and x in primeIds: # x in primeIds
                bMatchList[primeIds[x]] += [i]
    # print(bMatchList)

    matchL = [-1 for i in range(len(A))]
    matchR = [-1 for i in range(len(B))]
    visitedL = [-1 for i in range(len(A))]
    visitedR = [-1 for i in range(len(primeIds))]
    
    t = 0
    for i in range(len(a)):
        if match(i, i):
            t += 1
    return t
    
# if __name__ == '__main__':
print(getMaximumRemovals(A, B))

# test case #10: 94857
# test case #4: 1867
sys.stdin.close()
sys.stdin = stdin

