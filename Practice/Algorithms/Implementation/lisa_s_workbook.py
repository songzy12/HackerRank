n, k = [int(x) for x in raw_input().split()]
ts = [int(x) for x in raw_input().split()]

next_index = 1
count = 0
for i in range(n):
    cur_index = next_index
    next_index = cur_index + ts[i] / k + (1 if ts[i] % k else 0)
    for j, page in enumerate(range(cur_index, next_index)):
        if j*k + 1 <= page <= min((j+1)*k, ts[i]):
            count += 1
print count
