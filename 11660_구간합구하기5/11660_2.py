import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# (1, 1)부터 (N, N)까지
dp = [[0]*(N+1) for _ in range(N+1)]

#(1, 1)부터 (i, j)까지의 합 dp에 미리 넣어주기 (행 + 열 - 겹치는 부분)
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + arr[i][j]
print(dp)
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])