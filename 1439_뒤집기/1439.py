import sys
sys.stdin = open('input.txt')

S = input()
cnt = 0
# 겹치는 숫자 제외한 배열로 만들어주기
tmp = [S[0]]
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        tmp.append(S[i])

# 더 적게 바꿀 숫자 정하기 위해 카운트
zero = tmp.count('0')
one = tmp.count('1')

print(min(zero, one))