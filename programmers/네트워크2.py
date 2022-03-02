n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def dfs(v):
    visited[v] = 1

    for i in data[v]:
        if visited[i] == 0:
            dfs(i)


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
        dfs(i)

print(cnt)