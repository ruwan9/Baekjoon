import sys
sys.stdin = open('input.txt')

dp = [0]*1001
dp[1] = 1
dp[2] = 2
n = int(input())

for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
