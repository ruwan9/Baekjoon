import sys
sys.stdin = open('../inputs/1388.txt')

N, M = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(input()))

cnt = 0
for row in mat:
    for i in range(M-1):
        if row[i] == '-' and row[i+1] != '-':
            cnt += 1
    if row[-1] == '-':
        cnt += 1

# 2차원 리스트 뒤집기
new_mat = list(map(list, zip(*mat)))

for row in new_mat:
    for i in range(N-1):
        if row[i] == '|' and row[i+1] != '|':
            cnt += 1
    if row[-1] == '|':
        cnt += 1

print(cnt)