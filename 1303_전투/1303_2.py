import sys
sys.stdin = open('./input.txt')
from collections import deque


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
# print(arr)
# print(visited)
B, W = 0, 0

# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

# print(bfs(0, 0, 'W'))
# print(visited)

for i in range(M):
    for j in range(N):
        if visited[i][j] == False and arr[i][j] == 'W':
            W += bfs(i, j, 'W') ** 2
        if visited[i][j] == False and arr[i][j] == 'B':
            B += bfs(i, j, 'B') ** 2
print(W, B)