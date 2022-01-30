import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(x, y, ex, ey):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            print(arr[ex][ey]-1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y]+1

T = int(input())
for _ in range(T):
    I = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    arr = list([0]*I for _ in range(I))

    bfs(a, b, x, y)