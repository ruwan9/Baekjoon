import sys
sys.stdin = open('input.txt')

N = int(input())
lst = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    ans += lst[i]*(N-i)

print(ans)
