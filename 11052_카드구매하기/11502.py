import sys
sys.stdin = open('input.txt')

N = int(input())
cards = [0] + list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = cards[1]  # 1
dp[2] = max(cards[1]*2, cards[2])  # 2 vs 5

for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + cards[j]:
            dp[i] = dp[i-j] + cards[j]

print(dp[N])
