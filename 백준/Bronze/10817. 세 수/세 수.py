from heapq import heappush

from heapq import nlargest
heap1=[]
a,b,c=map(int,input().split())

heappush(heap1,a)
heappush(heap1,b)
heappush(heap1,c)
print(nlargest(2,heap1)[-1]) #n번째 큰 숫자까지 리스트로 반환 후 리스트[-1]출력
