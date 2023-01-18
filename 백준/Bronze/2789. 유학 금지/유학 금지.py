a=input()
b='CAMBRIDGE'

for i in b:
    if i in a:
        
        c=a.replace(i,'')
        a=c

print(a)