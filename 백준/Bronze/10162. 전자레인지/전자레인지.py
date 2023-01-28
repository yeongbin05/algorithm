s=int(input())
a_cnt=0
b_cnt=0
c_cnt=0

while s>=300:
    s-=300
    a_cnt+=1
while s>=60:
    s-=60
    b_cnt+=1
while s>=10:
    s-=10
    c_cnt+=1
if s!=0:
    print(-1)
else:
 print(a_cnt,b_cnt,c_cnt)