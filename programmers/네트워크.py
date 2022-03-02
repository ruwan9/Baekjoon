from collections import deque


def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in data[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

data = [[] for _ in range(n)]
visited = [0] * n
cnt = 0

for i in range(n):
    for j in range(n):
        if i != j and computers[i][j] == 1:
            data[i].append(j)

for i in range(n):
    if visited[i] == 0:
        cnt += 1
        bfs(i)

print(cnt)
