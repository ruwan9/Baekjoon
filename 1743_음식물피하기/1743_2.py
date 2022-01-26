import sys
sys.stdin = open('./input.txt')
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '#' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = '#'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '#' and visited[i][j] == 0:
            ans = max(ans, bfs(i, j))
print(ans)