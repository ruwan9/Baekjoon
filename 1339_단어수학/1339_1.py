import sys
sys.stdin = open('input.txt')

N = int(input())
words = [input() for _ in range(N)]

dic = {}
for word in words:
    s = len(word)
    for i in range(s):
        if word[i] in dic:
            dic[word[i]] += 10**(s-i-1)
        else:
            dic[word[i]] = 10**(s-i-1)

tmp = sorted(dic.values(), reverse=True)

res = 0
for i in range(len(tmp)):
    res += tmp[i]*(9-i)

print(res)