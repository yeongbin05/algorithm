import sys

a=int(input())

arr= [list(sys.stdin.readline().split()) for _ in range(a)]

arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in arr:
    sys.stdout.write(str(student[0]) + "\n")