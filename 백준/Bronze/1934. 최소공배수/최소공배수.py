t=int(input())
def max(n,m):
    while m!=0:
        num=n%m
        n=m
        m=num
    return n        
for i in range(t):
    a,b=map(int,input().split())
    
    print(int(a*b/max(a,b)))