import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] not in tmp:
                tmp.append(arr[nx][ny])
                dfs(nx, ny, cnt+1)
                tmp.remove(arr[nx][ny])
            print(tmp)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
tmp = [arr[0][0]]
ans = 0
dfs(0, 0, 1)
print(ans)
