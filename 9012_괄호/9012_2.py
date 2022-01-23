import sys
sys.stdin = open('./input.txt')

T = int(input())
for _ in range(T):
    stack = []
    cnt = 0
    data = list(input())
    # print(data)

    for i in data:
        if i == '(':
            stack.append(i)
            cnt += 1
        else:
            if not stack:
                cnt -= 1
                break
            else:
                if stack[-1] == '(':
                    cnt -= 1
                    stack.pop()

    if cnt == 0:
        print("YES")
    else:
        print("NO")