import sys
sys.stdin = open('input.txt')

N = int(input())
# 중복 제거
words = list(set(list(input() for _ in range(N))))

# 길이 먼저, 사전 순으로
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
