t=int(input())

for i in range(t):
    c=int(input())
    cnt_25=0 # 동전 갯수
    cnt_10=0 # 동전 갯수
    cnt_5=0 # 동전 갯수
    cnt_1=0 # 동전 갯수
    while c!=0:
        if c>=25:
            cnt_25+=c//25
            c-=(c//25*25)
        if c>=10:
            
            cnt_10+=c//10
            c-=(c//10*10)
        if c>=5:
            cnt_5+=c//5
            c-=(c//5*5)
        if c>=1:
            cnt_1+=c//1
            c-=(c//1*1)
    print(cnt_25,cnt_10,cnt_5,cnt_1)