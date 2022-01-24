import sys
sys.stdin = open('./input.txt')

T = int(input())
for _ in range(T):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])

