import sys
num=int(sys.stdin.readline())
who={}
for i in range(num):
    name,check=sys.stdin.readline().split()
    if name in who:
        who.pop(name)
    else:
        who[name]=check

# enter_person=[]
# for person in who:
#     # enter_person.append(person)
#     who.get(person)
# enter_person.sort()
# enter_person.reverse()
# for i in enter_person:
#     print(i)

person_reverse=sorted(who.items(),reverse=True)
for i in person_reverse:
    print(i[0])