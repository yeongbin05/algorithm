arr=[list(input()) for i in range(5)]


for j in range(15):
    for i in arr:
        try:
            print(i[j],end='')
        except:
            continue
        
        