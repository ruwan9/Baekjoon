import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global ans
    cnt = 1

    queue = set()
    queue.add((x, y, cnt, arr[0][0]))

    while queue:
        x, y, cnt, passed = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] not in passed:
                    queue.add((nx, ny, cnt+1, passed+arr[nx][ny]))
                    ans = max(ans, cnt+1)


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
ans = 1
bfs(0, 0)
print(ans)