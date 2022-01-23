import sys
sys.stdin = open('./input.txt')
# sys.setrecursionlimit(100000)


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


N, M = map(int, input().split())
# 인접행렬
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))  # 1씩 빼서 0부터 시작
    adj[a][b] = adj[b][a] = 1
print(adj)

ans = 0
chk = [False] * N

for i in range(N):
    if chk[i] == False:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)