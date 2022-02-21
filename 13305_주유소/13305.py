import sys
sys.stdin = open('input.txt')

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

# print(roads, prices)
res = 0
tmp = prices[0]
for i in range(N-1):
    tmp = min(prices[i], tmp)
    res += tmp * roads[i]

print(res)