num=int(input())
guest=list(map(int,input().split()))
reject_guest=set(guest)

print(len(guest)-len(reject_guest))
