import sys
sys.stdin = open('./input.txt')

N, K = map(int, input().split())
div = []

for i in range(1, N+1):
    if N % i == 0:
        div.append(i)

if len(div) < K:
    print(0)
else:
    print(div[K-1])
