import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)


def dfs(v):

    for i in tree[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)


N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

dfs(1)

for i in range(2, N+1):
    print(visited[i])
