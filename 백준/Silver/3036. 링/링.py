from fractions import Fraction
n=int(input())
a=list(map(int,input().split()))

for i in range(1,n):
    if a[0]%a[i]==0:
        print(str(Fraction(a[0],a[i]))+'/1')
    else:
        print(Fraction(a[0],a[i]))