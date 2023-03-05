T = int(input())
for t in range(T):
    n = int(input())
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i != 0:
            continue
        if i % 2 == 0:
            cnt += 1
        if n // i == i:
            continue
        if ((n // i) % 2 == 0):
            cnt += 1
    print(cnt)

# here we do not need to find all the prime powers
