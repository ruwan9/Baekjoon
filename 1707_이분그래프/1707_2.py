import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                queue.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    flg = 1
    for k in range(1, v+1):
        if visited[k]==0:
            if not bfs(k):
                flg = -1
                break
    print('YES' if flg==1 else 'NO')
    # ans = 'YES'
    # for i in range(1, K+1):
    #     if visited[i] == 0:
    #         if not bfs(i):
    #             ans = 'NO'
    #             break
    # print(ans)