import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    height = data[x][y]
    global cnt
    global tmp

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and data[nx][ny] > 0:
                # 현재 높이가 봉우리면
                if data[nx][ny] > height:
                    height = data[nx][ny]
                    tmp = True
                # 현재 높이가 주변 높이보다 낮으면 - 봉우리 아님
                if data[nx][ny] <= data[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    tmp = False
                # 현재 높이가 주변 높이보다 높으면 - 봉우리
                if data[nx][ny] > data[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
                    # print(nx, ny)


N, M = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(N))
visited = [[0]*M for _ in range(N)]
cnt = 0
tmp = False
print(data)
print(visited)

for i in range(N):
    for j in range(M):
        if data[i][j] > 0 and visited[i][j] == 0:
            bfs(i, j)
            if tmp:
                cnt += 1
            # print(i, j)

print(cnt)


# 산봉우리의 개념이 어려웠다.
