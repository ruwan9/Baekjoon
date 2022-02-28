import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
h = set()
for _ in range(N):
    h.add(input())
s = set()
for _ in range(M):
    s.add(input())

res = sorted(list(h & s))

print(len(res))
for i in res:
    print(i)