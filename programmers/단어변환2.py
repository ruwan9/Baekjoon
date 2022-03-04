begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def check(w1, w2):
    tmp = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            tmp += 1

    return True if tmp == 1 else False


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [0] * len(words)
    queue = [begin]

    while queue:
        word = queue.pop()
        if word == target:
            return answer

        for i in range(len(words)):
            if visited[i] == 0 and check(word, words[i]):
                visited[i] = 1
                queue.append(words[i])
        answer += 1


print(solution(begin, target, words))