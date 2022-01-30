import sys
sys.stdin = open('input.txt')

n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

s.sort(key=lambda a: a[0])
s.sort(key=lambda a: a[1])
# print(s)

last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)