import sys
sys.stdin = open('input.txt')

N = int(input())
timer = [300, 60, 10]

if N % 10:
    print(-1)
else :
    for time in timer:
        print(N//time, end=' ')
        N = N%time
