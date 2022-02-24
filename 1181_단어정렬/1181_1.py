import sys
sys.stdin = open('input.txt')

N = int(input())
words = list(set(list(input() for _ in range(N))))
words.sort()
words.sort(key=lambda x: len(x))

for word in words:
    print(word)
