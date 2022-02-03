import sys
sys.stdin = open('input.txt')

N = int(input())
weights = list(int(input()) for _ in range(N))
weights.sort(reverse=True)

ans = []
for i in range(N):
    ans.append(weights[i]*(i+1))

print(ans)