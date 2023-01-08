a=int(input())

# k층 n호
for i in range(a):
    k=int(input())
    n=int(input())
    
    
    people=[i for i in range(1,n+1)]
    
    for j in range(k):
        new_people=[]
        for k in range(n):
            new_people.append(sum(people[:k+1]))
        people=new_people.copy()
    print(people[-1])