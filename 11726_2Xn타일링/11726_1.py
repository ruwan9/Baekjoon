import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

def tile(n):
    if dp[n] == 0:
        dp[n] = tile(n-1) + tile(n-2)
    return dp[n]


n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

print(tile(n)%10007)