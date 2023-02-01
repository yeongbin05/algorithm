n=int(input())

while True:
    cnt=0
    
    for i in str(n):
        
        if i=='4' or i=='7':
            cnt+=1
            if cnt==len(str(n)):
                print(n)
                
        else:
            n-=1
            break
    if cnt==len(str(n)):
        break
    
