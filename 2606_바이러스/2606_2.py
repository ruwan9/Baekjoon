import sys
sys.stdin = open('../inputs/2606.txt')


def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


computers = int(input())
pairs = int(input())
visited = [0] * (computers+1)
graph = [[] for _ in range(computers+1)]

for _ in range(pairs):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

visited[1] = 1
dfs(1)
print(sum(visited)-1)