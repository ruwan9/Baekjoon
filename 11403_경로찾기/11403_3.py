import sys
sys.stdin = open('input.txt')


# 끝까지 가봐야하니까 dfs
def dfs(v):
    for i in range(N):
        if arr[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 번호(출발지점)에서 dfs
for i in range(N):
    # 방문 초기화
    visited = [0] * N
    dfs(i)

    print(*visited)