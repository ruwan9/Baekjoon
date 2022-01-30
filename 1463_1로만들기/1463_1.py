import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [-1]*(N+3)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    cnt = 10**6
    if i % 3 == 0:
        cnt = min(dp[i//3], cnt)
    if i % 2 == 0:
        cnt = min(dp[i//2], cnt)

    dp[i] = min(dp[i-1], cnt)+1

print(dp[N])