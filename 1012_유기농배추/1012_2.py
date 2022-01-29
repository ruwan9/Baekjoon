import sys
sys.stdin = open('./input.txt')
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                arr[i][j] = 0
                cnt += 1

    print(cnt)