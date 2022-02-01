import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, tmp):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and arr[nx][ny] > tmp:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for row in arr:
    max_height = max(max(row), max_height)

res = 1
for height in range(1, max_height+1):
    cnt = 0
    tmp = height
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > tmp:
                bfs(i, j, tmp)
                cnt += 1

    if res <= cnt:
        res = cnt

print(res)