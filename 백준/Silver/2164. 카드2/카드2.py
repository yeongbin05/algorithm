from collections import deque

a=int(input())
queue=deque() #queue 는 pop(0)시간복잡도 O(1) list는 O(n)
for i in range(1,a+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    # queue.append(queue[0])
    # queue.popleft()
    add=queue.popleft()
    queue.append(add)
    # print(queue)
    # if len(queue)==1:
    #     print(queue[0])
    #     break
print(queue[0])