import sys
sys.stdin = open('input.txt')

N = int(input())
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append([s, e])

# 끝 기준 먼저 정렬, 시작 기준 정렬
times.sort(key=lambda x: (x[1], x[0]))
print(times)

ans = 0
for i in range(N):
    cnt = 1
    tmp = times[i][1]
    for j in range(i, N):
        if times[j][0] >= tmp:
            tmp = times[j][1]
            cnt += 1
    if ans <= cnt:
        ans = cnt

print(ans)