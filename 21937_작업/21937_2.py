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


N, M = map(int, sys.stdin.readline().split())
data = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # 방향성 -> 역으로 추적하기
    data[B].append(A)
X = int(sys.stdin.readline())

visited = [0]*(N+1)
cnt = 0
dfs(X)

print(cnt)

# 뭐가 문제인지 한참 헤맸는데... 데이터 불러오는 방식을 sys.stdin.readline() 사용하니까 시간초과 해결...