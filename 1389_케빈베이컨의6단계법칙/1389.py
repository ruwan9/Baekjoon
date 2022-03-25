import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1


    while queue:
        v = queue.popleft()
        # print(visited)
        for i in data[v]:
            if visited[i] == 0:
                # 단계(횟수?) 구하기
                visited[i] = visited[v] + 1
                queue.append(i)


N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

# 케빈 베이컨 수
zero = float('inf')
res = [zero]  # 0번 인덱스 채우기

for i in range(1, N+1):
    visited = [0] * (N+1)
    bfs(i)
    # 유저 별 단계의 합 더해주기
    res.append(sum(visited) - visited[i])
    print(res)

print(res.index(min(res)))

print(int(-30/4))