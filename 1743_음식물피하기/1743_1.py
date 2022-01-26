import sys
sys.stdin = open('./input.txt')
sys.setrecursionlimit(10**8)


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == '#' and visited[nx][ny] == 0:
                dfs(nx, ny)



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
        cnt = 0
        if arr[i][j] == '#' and visited[i][j] == 0:
            dfs(i, j)
            ans = max(ans, cnt)
print(ans)