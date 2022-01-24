import sys
sys.stdin = open('./input.txt')

words = list((input()))
print(words)
tmp = 1
stack = []
res = 0

for i in range(len(words)):
    if words[i] == '(':
        stack.append(words[i])
        tmp *= 2

    elif words[i] == '[':
        stack.append(words[i])
        tmp *= 3

    elif words[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if words[i-1] == '(':
            res += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if words[i-1] == '[':
            res += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(res)