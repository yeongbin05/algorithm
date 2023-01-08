a=1
b=int(input())
for i in range(1,b+1):
    

    a=a+i+1
    if b==1:
        print('1/1')
        break
    if b<=a:
        if i %2!=0 :
            b=abs(b-a)
            print(str(2+i-b-1)+'/'+str(b+1))
            # print("홀수")
            break
        else:
            b=abs(b-a)
            print(str(b+1)+'/'+str(2+i-b-1))
            # print("짝수")
            break
