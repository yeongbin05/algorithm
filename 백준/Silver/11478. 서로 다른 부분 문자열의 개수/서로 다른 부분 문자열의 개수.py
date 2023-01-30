a=input()

result=set(a) # 결과에서 똑같은거 제외

for i in range(len(a)):
    for j in range(i,len(a)):
        subtotal=a[i:j+1]
        result.add(subtotal)

print(len(result))