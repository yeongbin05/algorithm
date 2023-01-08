
a=int(input())

for i in range(a):
    h,w,n=map(int,input().split())
    num=n//h+1
    num1=n%h
    if n%h==0:
        num=n//h
        num1=h
    print(num1*100+num)