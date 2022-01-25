import sys
sys.stdin = open('./input.txt')


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

# M 이상 N 이하
primes = []
for i in range(M, N+1):
    if is_prime(i):
        primes.append(i)

print(primes)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)