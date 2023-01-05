a=[]
for i in range(10001):
    a.append(i+1)
b=[]
cnt=0
cnt1=0
for i in range(10001):
    for j in range(len(str(i))):
        cnt=cnt+int(str(i)[j])
        
    b.append((i+cnt))
    cnt=0
    # cnt1+=1
    # print("cnt1 > " +str(cnt1))
    

for i in b:
    if i in a:
        a.remove(i)
for i in a:
    print(i)
