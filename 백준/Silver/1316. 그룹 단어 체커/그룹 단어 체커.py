num=int(input())
cnt=0

for i in range(num):
    alphabet={}
    a=input()
    for j in range(len(a)):
        if a[j] not in alphabet:
            
            alphabet[a[j]]=1
            
        elif  a[j] in alphabet and a[j-1]!= a[j]:
            cnt+=1
            break
            

        elif a[j] in alphabet:
            alphabet[a[j]]+=1
            
        
        
    
print(num-cnt)
