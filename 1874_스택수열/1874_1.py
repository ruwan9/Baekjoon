import sys
sys.stdin = open('input.txt')

n = int(input())
stack = []
ans = []
tmp = 1
for i in range(1, n+1):
    num = int(input())
    while tmp <= num:
        stack.append(tmp)
        ans.append('+')
        tmp += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')

if not stack:
    for i in ans:
        print(i)
else:
    print('NO')