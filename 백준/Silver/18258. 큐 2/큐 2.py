import sys
from collections import deque
a=int(sys.stdin.readline())
list1=deque()

for i in range(a):
    
    
    order=sys.stdin.readline().split()
    if order[0]=='push':
        list1.append(int(order[1]))
   
      
    
    elif order[0]=='front':
        if len(list1)!=0:
            print(list1[0])
        else:
            print(-1)

    elif order[0]=='size':
        print(len(list1))

    elif order[0]=='empty':
        if len(list1)==0:
            print(1)
        else:
            print(0)

    elif order[0]=='pop':
        if len(list1)!=0:
            # popped=list1[-1]
            # list1.remove(list1[-1])  # remove는 리스트에서 해당 첫번째 원소를 삭제해서 안됨
            # print(popped)
            print(list1.popleft())
        else:
            print(-1)
    
    elif order[0]=='back':
        if len(list1)!=0:
            print(list1[-1])
        else:
            print(-1)