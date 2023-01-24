import sys
a=int(sys.stdin.readline())
list1=[]
for i in range(a):
    list1.append(int(sys.stdin.readline()))

list1_reverse=reversed(sorted(list1))

for j in list1_reverse:
    print(j)