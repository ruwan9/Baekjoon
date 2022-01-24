import sys
sys.stdin = open('./input.txt')

tmp = 0
cnt = 0
for _ in range(10):
    o, i = map(int, input().split())
    tmp = tmp + i - o

    if cnt < tmp:
        cnt = tmp

print(cnt)
