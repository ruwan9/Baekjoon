import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0]*10001

dp[1] = 1
dp[2] = 3
dp[3] = dp[1]*2 + dp[2]

for i in range(3, n+1):
    dp[i] = dp[i-2]*2 + dp[i-1]


print(dp[n]%10007)