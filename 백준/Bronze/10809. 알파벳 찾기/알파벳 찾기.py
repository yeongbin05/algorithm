a=input()
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in b:
    if i in a:
        print(a.index(i), end=' ')
    else:
        print(-1,end=' ')
