import sys
sys.stdin = open('./input.txt')


def dfs(idx, cnt):
    visited[idx] = 1

    for i in graph[idx]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)

    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(dfs(1, 0))