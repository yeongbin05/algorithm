from sys import stdin
a=int(stdin.readline())
list=[]

for i in range(a):
    list.append(int(stdin.readline()))

list1=[]
b=int(stdin.readline())

for i in range(b):
    list1.append(int(stdin.readline()))

list2=[]
c=int(stdin.readline())

for i in range(c):
    list2.append(int(stdin.readline()))

if sum(list)==0:
    print(0)
elif sum(list)>0:
    print("+")
else :
    print("-")

if sum(list1)==0:
    print(0)
elif sum(list1)>0:
    print("+")
else :
    print("-")

if sum(list2)==0:
    print(0)
elif sum(list2)>0:
    print("+")
else :
    print("-")