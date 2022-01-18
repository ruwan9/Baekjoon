import sys
sys.stdin = open('inputs/1449.txt')

N, L = map(int, input().split())
s = sorted(list(map(int, input().split())))

start = s[0]
end = s[0] + L
cnt = 1
for i in range(N):
    if start <= s[i] < end:
        continue
    else:
        start = s[i]
        end = s[i] + L
        cnt += 1
print(cnt)