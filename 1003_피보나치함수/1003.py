import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    dp_zero = [1, 0, 1]
    dp_one = [0, 1, 1]
    for i in range(3, N+1):
        dp_zero.append(dp_zero[i-1]+dp_zero[i-2])
        dp_one.append(dp_one[i-1]+dp_one[i-2])

    print(dp_zero[N], end=' ')
    print(dp_one[N])