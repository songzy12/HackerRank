from math import factorial

n=int(raw_input())
for i in range(n):
    a,b=map(int,raw_input().split())
    print (factorial(a+b-1)/(factorial(a)*factorial(b-1)))%1000000007

# 测试所设的时限也太松了点
