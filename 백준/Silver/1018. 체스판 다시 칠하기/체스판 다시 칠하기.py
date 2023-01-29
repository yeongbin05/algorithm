# M*N 크기의 보드 내에서 새로 칠해야 하는 부분이 가장 적은 정사각형 8*8부분 고르기
import copy
M,N=map(int,input().split())

board=[list(input()) for i in range(M)]  # 전체 보드
  #복사
cnt_lst=[]
 #색을 바꿔야하는 정사각형 수
# print(board)
# 8*8 보드
cnt1=0
for x in range(M-7):
    
    for y in range(N-7):
        
        copy_board=copy.deepcopy(board)
        cnt=0  # B로시작
        cnt1=0 # W로시작
        for i in range(x,x+8):
            for j in range(y,y+8):
                if (i+j)%2==0:
                    if copy_board[i][j]!='B':
                        cnt+=1
                    else:
                        cnt1+=1
                else:
                    if copy_board[i][j]!='W':
                        cnt+=1
                    else:
                        cnt1+=1
        cnt_lst.append(cnt)
        cnt_lst.append(cnt1)
        # for i in copy_board:
        #     print(i)
        # print('==============================')
print(min(cnt_lst))

# print(board)
# print(copy_board[7])
