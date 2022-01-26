import sys
sys.stdin = open('./input.txt')
from collections import deque

A, B = map(int, input().split())
# 곱하기 2
# 곱하기 10 더하기 1

queue = deque()
queue.append((A, 1))

while queue:
    x, t = queue.popleft()
    if x == B:
        print(t)
        exit()

    if x*2 <= B:
        queue.append((x*2, t+1))

    if x*10+1 <= B:
        queue.append((x*10+1, t+1))

print(-1)


