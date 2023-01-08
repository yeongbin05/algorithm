a,b,c=map(int,input().split())
cnt=0

if b<c:
    a=a/(c-b)
    print(int(a)+1)
    
if b>c or b==c:
    print(-1)
    
