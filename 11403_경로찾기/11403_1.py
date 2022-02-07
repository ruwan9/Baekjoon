import sys
sys.stdin = open('input.txt')


def dfs(v):
    for i in range(N):
        if arr[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


N = int(input())
visited = [0]*N
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
    visited = [0]*N