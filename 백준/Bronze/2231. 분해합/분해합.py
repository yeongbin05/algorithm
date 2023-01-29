import sys
n=int(sys.stdin.readline())
cnt=0
sm=0
while True:
    cnt+=1
    sm=0
    for i in str(cnt):
        sm+=int(i)
    sm+=int(cnt)
    if sm==n:
        break
    if cnt>n:
        break

if sm==n:
        print(cnt) 
elif cnt>n:
    print(0)