import sys
sys.stdin = open('input.txt')

K = int(input())

tmp = []
for _ in range(K):
    num = int(input())
    if num != 0:
        tmp.append(num)
    else:
        tmp.pop()

print(sum(tmp))