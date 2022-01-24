import sys
sys.stdin = open('./input.txt')


def fiv(num):
    if num < 2:
        return num
    else:
        return fiv(num-1) + fiv(num-2)


n = int(input())
print(fiv(n))
