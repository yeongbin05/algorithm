from sys import stdin
a,b=map(int, stdin.readline().split())


for i in range(a,b+1):
    
    if i==1:
        
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            
            break
    else: 
        print(i)