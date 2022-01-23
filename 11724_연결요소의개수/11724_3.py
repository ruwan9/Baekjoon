import sys
sys.stdin = open('./input.txt')


def dfs(v):
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if visited[i] == False:
        cnt += 1
        visited[i] = True
        dfs(i)

print(cnt)