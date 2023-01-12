from sys import stdin
a=input()
b=[]
for i in a:
    b.append(int(i))
b.sort()
b.reverse()
for i in b:
    print(i,end='')