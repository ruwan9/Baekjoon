import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)


def dfs(v):
    global cnt
    visited[v] = 1

    for i in data[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    # 방향성 -> 역으로 추적하기
    data[B].append(A)
X = int(input())

visited = [0]*(N+1)
cnt = 0

if not data[X]:
    print(0)
else:
    dfs(X)
    print(cnt)



# 시간초과...