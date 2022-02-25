import sys
sys.stdin = open('input.txt')

while True:
    data = input()
    if data == '.':
        break
    stack = []
    tmp = True

    for char in data:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                tmp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                tmp = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if tmp and not stack:
        print("yes")
    else:
        print("no")