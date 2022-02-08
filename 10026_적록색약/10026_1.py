import sys
sys.stdin = open('input.txt')
from collections import deque


def rgb(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'G':
                arr[i][j] = 'R'



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and arr[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            cnt += 1
        if arr[i][j] == 'G' and visited[i][j] == 0:
            bfs(i, j, 'G')
            cnt += 1
        if arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            cnt += 1
print(cnt, end=' ')

rgb(arr)
visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            cnt += 1
        if arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            cnt += 1
print(cnt)