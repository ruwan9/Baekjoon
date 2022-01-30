import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1


M, N = map(int, input().split())
arr = []
for _ in range(N):
    lst = list(map(int, input().split(' ')))
    arr.append(lst)
print(arr)

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))

bfs()

ans = 0
for row in arr:
    for i in row:
        if i == 0:
            print(-1)
            exit()
    ans = max(ans, max(row))
print(ans-1)