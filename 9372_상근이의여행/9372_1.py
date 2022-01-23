import sys
sys.stdin = open('./input.txt')


def dfs(v):
    global cnt
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
            cnt += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    print(visited)

    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)

    print(cnt)
