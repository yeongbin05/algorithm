word=list(input())
arr=[]
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        front=''.join(word[:i])
        front=front[::-1]
        middle=''.join(word[i:j])
        middle=middle[::-1]
        end=''.join(word[j:])
        end=end[::-1]
        # print(front,middle,end)
        arr.append(front+middle+end)

arr.sort()
print(arr[0])