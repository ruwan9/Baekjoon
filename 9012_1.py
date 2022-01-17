import sys
sys.stdin = open('inputs/9012.txt')

T = int(input())
for _ in range(T):
    stack = []
    ans = ''
    data = input()
    # print(data)

    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'NO'
                break
    # print(stack, ans)
    if ans != 'NO' and not stack:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)