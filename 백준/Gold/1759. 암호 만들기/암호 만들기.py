from itertools import combinations

l,c=map(int,input().split())
vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
arr=input().split()
comb=list(combinations(arr,l))

new_arr=[]
result=[]
for i in comb:
    new_arr.append(sorted(i))

new_arr.sort()


for j in new_arr:
    
    cnt_vowels,cnt_consonants=0,0
    for k in j:
        if k in vowels:
            cnt_vowels+=1
        if k in consonants:
            cnt_consonants+=1
    if cnt_vowels>=1 and cnt_consonants>=2:
        result.append(j)
        



for a in result:
    for b in a:
        print(b,end='')
    print()