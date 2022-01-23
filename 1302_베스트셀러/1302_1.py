import sys
sys.stdin = open('./input.txt')

N = int(input())
books = list(input() for _ in range(N))

dic = {}
for book in set(books):
    dic[book] = books.count(book)

ans = []
for k, v in dic.items():
    if v == max(dic.values()):
        ans.append(k)
print(sorted(ans)[0])
