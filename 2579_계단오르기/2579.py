import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [0] * 301
for i in range(1, N+1):
    lst[i] = int(input())

dp = [0] * 301

dp[1] = lst[1]  # 10
dp[2] = lst[1] + lst[2]  # 30
dp[3] = max(lst[1]+lst[3], lst[2]+lst[3])  # 35

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2]+lst[i])

print(dp[N])