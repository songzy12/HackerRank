f=[1,1,-2,-6,24,120,-720,-5040,40320,362880]
N = int(input())
for n in range(N):
    print('%.3f\n%.3f\n'%(sum([3**i/f[i] for i in range(1,10,2)]), sum([3**i/f[i] for i in range(0,9,2)])))
    map(lambda x:print(x), input())
    map(lambda x:print('%.3f\n%.3f\n'%(sum([x**i/f[i] for i in range(1,10,2)]), sum([x**i/f[i] for i in range(0,9,2)]))), float(input()))
