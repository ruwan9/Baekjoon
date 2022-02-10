import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if container[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    container[nx][ny][nz] = container[x][y][z] + 1

# 가로, 세로, 높이
M, N, H = map(int, input().split())
container = []
cnt = 0
queue = deque()
for _ in range(H):
    arr = [list(map(int, input().split())) for _ in range(N)]
    container.append(arr)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if container[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if container[i][j][k] == 0:
                print(-1)
                exit()

ans = 0
for i in container:
    for j in i:
        ans = max(max(j), ans)

print(ans-1)