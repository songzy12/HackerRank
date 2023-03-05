# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

from math import sqrt 

T = int(input().strip())

primes= [2,3] # put all this outside the for loop
length = len(primes)
t = 5

for a0 in range(T): # NOTE: do not use the same name
    n = int(input().strip())

    
    def check(t):
        for i in primes:
            if i>sqrt(t):
                return True
            if t%i==0:
                return False

    while length < n:
        if check(t):
            primes.append(t)
            length += 1
        t+=2

    print(primes[n-1]) # since #primes may be more than n
