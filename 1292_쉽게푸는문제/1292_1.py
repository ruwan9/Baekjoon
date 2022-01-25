import sys
sys.stdin = open('./input.txt')

A, B = map(int, input().split())
arr = []
for i in range(1, 1000):
    tmp = i
    while tmp > 0:
        arr.append(i)
        tmp -= 1
# print(arr)
if A == B:
    print(arr[A-1])
else:
    print(sum(arr[A-1:B]))