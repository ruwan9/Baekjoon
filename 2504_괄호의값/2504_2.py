import sys
sys.stdin = open('./input.txt')


def bracket_check(words):
    dic = {')': '(', ']': '['}
    stack = []
    for char in words:
        if char not in dic:
            stack.append(char)
        elif not stack or dic[char] != stack.pop():
            return False
    return True


def calc(words):
    stack = []
    tmp = 1
    ans = 0
    for i in range(len(words)):
        if words[i] == '(':
            stack.append('(')
            tmp *= 2
        elif words[i] == '[':
            stack.append('[')
            tmp *= 3
        elif words[i] == ')':
            if words[i-1] == '(':
                ans += tmp
            stack.pop()
            tmp //= 2
        elif words[i] == ']':
            if words[i-1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
    return ans


words = list((input()))
print(words)
tmp = 0

if bracket_check(words):
    print(calc(words))
else:
    print(0)
