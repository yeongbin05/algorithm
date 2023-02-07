
row=['A','B','C','D','E','F','G','H']
col=['8','7','6','5','4','3','2','1']

dic={
    'R':(1,0),
    'L':(-1,0),
    'B':(0,-1),
    'T':(0,1),
    'RT':(1,1),
    'LT':(-1,1),
    'RB':(1,-1),
    'LB':(-1,-1),
}

arr=[['']*8 for i in range(8)]

king,stone,n=input().split()
n=int(n)
king_row=col.index(king[1])
king_col=row.index(king[0])
stone_row=col.index(stone[1])
stone_col=row.index(stone[0])

# arr[king_row][king_col]='K'
# arr[stone_row][stone_col]='S'

# for i in arr:
#     print(i)
for i in range(n):
    move=input()
    if 0<=king_row-dic[move][1]<8 and 0<=king_col+dic[move][0]<8:
        #위치 겹칠 때
        if king_row-dic[move][1]==stone_row and king_col+dic[move][0]==stone_col:
            #stone이 배열 밖으로 안나갈때
            if 0<=stone_row-dic[move][1]<8 and 0<=stone_col+dic[move][0]<8:
                king_row-=dic[move][1]
                king_col+=dic[move][0]
                stone_row-=dic[move][1]
                stone_col+=dic[move][0]
        else:
            king_row-=dic[move][1]
            king_col+=dic[move][0]
# print(king_row,king_col)
print(row[king_col]+col[king_row])
# print(stone_row,stone_col)
print(row[stone_col]+col[stone_row])