from collections import deque
test_case=int(input())

for i in range(test_case):
    cnt=0
    a,b=map(int,input().split())

    c=deque(map(int,input().split()))
    c_= [0 for i in range(a)]
    c_[b]=1#deque로하면 오류
    while True:
        
        if c[0]==max(c):
            if c_[0]==1:
                cnt+=1
                print(cnt)
                break
                
            c.popleft()
            c_.pop(0)
            # print(c)
            cnt+=1
            
            
        else:
            c.append(c.popleft())
            c_.append(c_.pop(0))
            # print(c,end=' ')
            # print(c_)
            
