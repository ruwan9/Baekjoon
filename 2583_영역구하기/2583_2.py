import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    tmp = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    tmp += 1
    return tmp


M, N, K = map(int, input().split())
arr = []
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    arr.append(list(map(int, input().split())))

# print(arr)
# print(visited)
# 0, 2 -> 2, 0 / 1, 1 -> 3, 1 / 4, 0 -> 4, 4
for data in arr:
    for x in range(data[0], data[2]):
        for y in range(data[1], data[3]):
            # print(M-y-1, x)
            if visited[M-y-1][x] == 0:
                visited[M-y-1][x] = 1
# print(visited)
cnt = 0
ans = []
for j in range(N):
    for i in range(M):
        if visited[i][j] == 0:
            ans.append(bfs(i, j))
            # print(bfs(i, j), end=" ")
            cnt += 1
# print(visited)
print(cnt)
print(*ans)