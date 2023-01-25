###투포인터로 다시풀기
import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))# 투포인터쓰려면 sort써야하는데 deque는 sort안됨
x=int(sys.stdin.readline())

a.sort()
start=0
total=0
end=len(a)-1

while start<end:
    subtotal=a[start]+a[end]
    if subtotal==x:
        total+=1
        start+=1
        end-=1
    elif subtotal<x:
        start+=1
    else:
        end-=1

print(total)