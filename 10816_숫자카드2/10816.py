import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
answers = list(map(int, input().split()))

# for answer in answers:
#     print(numbers.count(answer), end=' ')

dic = dict()

for i in numbers:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(M):
    if answers[i] in dic:
        print(dic[answers[i]], end=' ')
    else:
        print(0, end=' ')