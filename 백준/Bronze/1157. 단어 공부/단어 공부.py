a=input()
dic={}
for i in a:
    if i.lower() in dic:
        dic[i.lower()]+=1
    else:
        dic[i.lower()]=1

max=0
value=''
for i in dic:
    
    if dic[i.lower()]>max:
        max=dic[i]
        value=i

    if dic[i.lower()]==max:
        
        if i.upper()==value.upper():
            continue
        
        value='?'
        
print(value.upper())
    

