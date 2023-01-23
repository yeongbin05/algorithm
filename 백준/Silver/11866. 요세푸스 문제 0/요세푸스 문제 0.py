n,k=map(int,input().split())

list1=[]
for i in range(1,n+1):
    list1.append(i)  #1~n 생성

list2=[]
while len(list2)!=n:
    for i in range(k-1):
        list1.append(list1.pop(0))  #k-1만큼 왼쪽에서 뺴고 오른쪽으로 추가
    list2.append(list1.pop(0)) # 뺀 후 가장 왼쪽값 추가

print('<',end='')
for i in range(len(list2)-1):
    print(list2[i],end=', ')
print(list2[-1],end='')
print('>')