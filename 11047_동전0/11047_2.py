import sys
sys.stdin = open('./input.txt')

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
coins.reverse()
# print(coins)

ans = 0
for coin in coins:
    ans += K // coin
    K %= coin

print(ans)