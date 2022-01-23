import sys
sys.stdin = open('./input.txt')


def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


computers = int(input())
pairs = int(input())
visited = [0] * (computers+1)
graph = [[] for _ in range(computers+1)]

for _ in range(pairs):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)


dfs(1)
print(sum(visited)-1)