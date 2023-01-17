a=int(input())
list=[0]*(a+1) # 첫번째수가 0번째로 주어졌으므로 a+1만큼 리스트 생성

if a>=2: #a가 0이나 1일경우 제외
    list[0],list[1]=0,1 #0번,1번은 미리 할당
else:
    pass
for i in range(2,a+1):
    list[i]=list[i-2]+list[i-1]

if a==0:
    print(0)
elif a==1:
    print(1)
else:
    print(list[a])
