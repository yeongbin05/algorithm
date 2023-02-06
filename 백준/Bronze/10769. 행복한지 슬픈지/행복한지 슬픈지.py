# replace함수 쓰는법
n=input()
smile_cnt=0
sad_cnt=0

while ':-)' in n:
    n=n.replace(':-)','',1)
    smile_cnt+=1
    

while ':-(' in n:
    n=n.replace(':-(','',1)
    sad_cnt+=1
    

if sad_cnt ==0 and smile_cnt ==0:
    print('none')

elif smile_cnt==sad_cnt:
    print('unsure')
elif smile_cnt>sad_cnt:
    print('happy')
else:
    print('sad')