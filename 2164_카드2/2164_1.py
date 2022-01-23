import sys
sys.stdin = open('./input.txt')
from collections import deque

N = int(input())
dq = deque()
for i in range(1, N+1):
    dq.append(i)
# print(dq)

while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)
print(dq[0])