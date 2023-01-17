a=int(input()) #
b=list(map(int,input().split()))
dic={} #숫자마다 고유값 설정하기위해 dic
c=list(set(b)) #중복을 제거하고 set타입을 리스트로 바꾼다
c.sort() #가장 작은것부터 0을 부여하기위해

cnt=0
for i in c:
    dic[i]=cnt
    cnt+=1

for i in b:
    print(dic[i],end=' ')