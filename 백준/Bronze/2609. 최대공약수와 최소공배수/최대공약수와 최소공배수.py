import sys
a,b=map(int,sys.stdin.readline().split())
c=a
d=b
gcd=0
while True:
    num=c%d
    c=d
    d=num
    if d==0:
        print(c)
        gcd=c
        break

print(int(a*b/gcd))