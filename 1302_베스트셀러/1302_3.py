import sys
sys.stdin = open('../inputs/1302.txt')

N = int(input())
books = list(input() for _ in range(N))
book_lst = sorted(list(set(books)))

cnts = []

for book in book_lst:
    cnts.append(books.count(book))

idx = cnts.index(max(cnts))
print(book_lst[idx])