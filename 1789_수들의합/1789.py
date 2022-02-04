import sys
sys.stdin = open('input.txt')

S = int(input())
N = 0

while True:
    if N * (N+1)/2 <= S and (N+1)*(N+2)/2 > S:
        print(N)
        break
    else:
        N += 1