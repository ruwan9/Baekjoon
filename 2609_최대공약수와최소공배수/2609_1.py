import sys
sys.stdin = open('./input.txt')


def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n


def lcm(n, m):
    return (n * m)//gcd(n, m)


n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))