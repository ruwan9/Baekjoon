import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[x][y] == 0:
                dfs(nx, ny)
                visited[x][y] = 1


N, M = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(N))
visited = [[0]*M for _ in range(N)]
cnt = 0
tmp = False
print(data)
print(visited)