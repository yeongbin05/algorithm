a=int(input())

num=0
cnt=0
while a!=cnt:
    num+=1
    if '666' in str(num): #연속된 6을 찾기 위해서
        cnt+=1
print(num)
