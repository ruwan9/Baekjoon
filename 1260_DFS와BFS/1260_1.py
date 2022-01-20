import sys
sys.stdin = open('../inputs/1260.txt')
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in sorted(graph[v]):
        if visited[i] == False:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in sorted(graph[v]):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
# print(graph)

dfs(graph, V, visited)
visited = [False] * (N+1)
print()
bfs(graph, V, visited)


