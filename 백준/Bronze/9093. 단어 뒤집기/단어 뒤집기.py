a=int(input())

for i in range(a):
    list1=input().split()
    for i in list1:
        print(i[::-1],end=' ')
    print()
