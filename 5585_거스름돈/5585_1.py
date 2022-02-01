import sys
sys.stdin = open('input.txt')

money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
i = 0

while i < 6:
    cnt += money // coins[i]
    money = money % coins[i]
    i += 1

print(cnt)