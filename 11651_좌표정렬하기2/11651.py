import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(*data[i])