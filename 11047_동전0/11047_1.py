import sys
sys.stdin = open('./input.txt')

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))

cnt = 0
while K:
    for coin in coins[::-1]:
        if coin <= K:
            cnt += (K // coin)
            K %= coin

print(cnt)