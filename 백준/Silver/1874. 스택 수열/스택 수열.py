import sys
n=int(sys.stdin.readline())
arr=[]
stack=[]
ans=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))


for i in range(1,n+1):
    stack.append(i)
    ans.append('+')
    while stack:
        
        if stack[-1]==arr[0]:
            stack.pop()
            arr.pop(0)
            ans.append('-')
            
        else:
            break
if len(stack)>0:
    print('NO')
else:
    print(*ans,sep='\n')