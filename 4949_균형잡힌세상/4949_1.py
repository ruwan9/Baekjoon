import sys
sys.stdin = open('input.txt')

while True:
    data = input()
    if data == '.':
        break
    stack = []

    for char in data:
        if char == '(' or char =='[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if stack:
        print('no')
    else:
        print('yes')
