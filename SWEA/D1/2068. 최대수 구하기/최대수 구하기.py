a=int(input())
for i in range(1,a+1):
    list1=list(map(int,input().split()))
    print('#'+str(i),max(list1))