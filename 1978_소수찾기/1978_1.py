import sys
sys.stdin = open('./input.txt')


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if is_prime(i):
        cnt += 1

print(cnt)