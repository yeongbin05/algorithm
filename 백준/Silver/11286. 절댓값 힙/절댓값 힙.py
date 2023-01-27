from heapq import heappush
from heapq import heappop
import sys
a=int(sys.stdin.readline())
heap=[]
for i in range(a):
    b=int(sys.stdin.readline())
    if b==0:
        if len(heap)==0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap,(abs(b),b))