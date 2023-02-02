w=[]
k=[]
for i in range(10):
    w.append(int(input()))

for i in  range(10):
    k.append(int(input()))

w.sort()
k.sort()
w_score=[]
k_score=[]

w_score.append(w[7:])
k_score.append(k[7:])

print(sum(w_score[0]),sum(k_score[0]))
