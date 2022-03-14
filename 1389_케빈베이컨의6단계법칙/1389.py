import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in data[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
visited = [0] * (N+1)
res = []
print(data)

for _ in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

print(data)
bfs(1)
print(visited)