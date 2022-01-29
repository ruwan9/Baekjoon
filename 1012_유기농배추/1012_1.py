import sys
sys.stdin = open('./input.txt')
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    # print(arr)
    # print(visited)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # print(bfs(0, 0))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)