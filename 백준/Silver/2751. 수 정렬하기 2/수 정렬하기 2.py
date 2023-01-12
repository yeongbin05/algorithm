from sys import stdin
a=int(stdin.readline())
b=[]
for i in range(a):
    b.append(int(stdin.readline()))
b.sort()
for i in b:
    print(i)