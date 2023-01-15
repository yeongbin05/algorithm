from sys import stdin
a=int(stdin.readline())
b=[]
for i in range(a):
    b.append(list(map(int,stdin.readline().split())))

b.sort(key=lambda x : (x[1],x[0]))
for i in b:
    print(i[0],i[1])