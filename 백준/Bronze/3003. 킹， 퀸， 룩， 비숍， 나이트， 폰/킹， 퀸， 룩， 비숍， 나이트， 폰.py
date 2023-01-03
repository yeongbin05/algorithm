chess = [1,1,2,2,2,8]
a=list(map(int,(input().split())))

for stone in range(6):
    print(chess[stone]-a[stone])