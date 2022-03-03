from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [0] * len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            tmp = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1
    return answer

print(solution(begin, target, words))