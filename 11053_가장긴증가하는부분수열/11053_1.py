import sys
sys.stdin = open('input.txt')

A = int(input())
numbers = list(map(int, input().split()))
print(numbers)

dp = [1]*A
print(dp)

for i in range(A):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp[-1])