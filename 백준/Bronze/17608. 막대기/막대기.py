import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

new_arr=[]
cnt=0
new_arr.append((arr)[-1])


for i in reversed(arr):
    
    if i>new_arr[-1]:
        new_arr.append(i)
        cnt+=1

print(cnt+1)
