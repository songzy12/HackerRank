import sys
stdin, stdout = sys.stdin, sys.stdout
fin = open('in.txt', 'r')
fout = open('out.txt', 'w')
sys.stdin = fin
# sys.stdout = fout

T = int(input())
for t in range(T):
    ladder_snake = [0 for i in range(101)]
    N = int(input())
    for n in range(N):
        start, end = map(int, input().split())
        ladder_snake[start] = end 
    M = int(input())
    for m in range(M):
        start, end = map(int, input().split())
        ladder_snake[start] = end

    
    visited = [False for i in range(101)]
    step = [0 for i in range(101)]
    
    Q = [1]
    answer = -1
    while Q:
        cur = Q.pop(0)
        visited[cur] = True
        if cur == 100:
            answer = step[cur]
            break
        for i in range(1,7):
            nex = cur + i
            if nex > 100:
                continue
            if ladder_snake[nex]:
                nex = ladder_snake[nex]
            if visited[nex]:
                continue
            visited[nex] = True
            step[nex] = step[cur] + 1
            Q += [nex]
    print(answer)

fin.close()
fout.close()
sys.stdin, sys.stdout = stdin, stdout
