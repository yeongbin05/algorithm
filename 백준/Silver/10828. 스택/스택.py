import sys
a=int(sys.stdin.readline())
list1=[]

for i in range(a):
    
    
    order=sys.stdin.readline().split()
    if order[0]=='push':
        list1.append(int(order[1]))
   
      
    
    elif order[0]=='top':
        if len(list1)!=0:
            print(list1[-1])
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
            # list1.remove(list1[-1])
            # print(popped)
            print(list1.pop())
        else:
            print(-1)