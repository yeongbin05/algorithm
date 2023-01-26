a=int(input())
arr=[0]*(a+1)
# arr[0]=0
# arr[1]=0
# arr[2]=1
# arr[3]=1
    
def function():
    for i in range(2,a+1):
        if i%3==0 and i%2==0:

            arr[i]=min(arr[i-1],arr[i//3],arr[i//2])+1
        elif i%2==0:
            arr[i]=(1+min(arr[i-1],arr[i//2]))
        elif i%3==0:
            arr[i]=(1+min(arr[i//3],arr[i-1]))
        else:
            arr[i]=(1+arr[i-1])
    return arr    

function()

print(arr[a])