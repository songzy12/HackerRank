T = int(input())
for t in range(T):
    N = int(input())
    prime = 1
    while N != 1:
        if prime * prime > N:
            break
        prime += 1
        if N % prime != 0:
            continue
        while N % prime == 0:
            # just like seive
            # not prime, not divisible
            N //= prime
    if N != 1:
        prime = N
    print(prime)

# Fermat: N = ab, then N = ((a+b)/2)^2-((a-b)/2)^2
# So try a = \sqrt{N}, compute b2 = a^2 - N
