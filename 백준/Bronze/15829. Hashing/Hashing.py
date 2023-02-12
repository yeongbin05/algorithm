a=int(input())

str=input()

result=[]

for i in range(a):
    result.append((ord(str[i])-96)*(31**i))

print(sum(result)%1234567891)