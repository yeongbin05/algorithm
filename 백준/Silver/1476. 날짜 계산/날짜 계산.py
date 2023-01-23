import sys
e,s,m=map(int,sys.stdin.readline().split())

e_,s_,m_=0,0,0
cnt=0
while e_!=e or s_!=s or m_!=m:
    
    if e_==15:
        e_=1
    else:
        e_+=1
    if s_==28:
        s_=1
    else:
        s_+=1
    if m_==19:
        m_=1
    else:
        m_+=1
    
    cnt+=1
    
print(cnt)
