import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])
res = []

while people:
    people.rotate(-K)
    res.append(str(people.pop()))

print("<", ", ".join(res), ">", sep="")