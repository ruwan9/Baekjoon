from collections import deque


def bfs(begin):
    global cnt
    queue = deque([begin])

    while queue:
        start = queue.popleft()

        if start == target:
            cnt += 1
            break

        for i in range(len(words)):
            if check(start, words[i]) and visited[i] == 0:
                cnt += 1
                queue.append(words[i])
                visited[i] = 1
                print(start, words[i], visited, queue)


def check(w1, w2):
    tmp = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            tmp += 1

    return True if tmp == 1 else False


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
cnt = 0
visited = [0 for _ in range(len(words))]
print(visited)

bfs(begin)
print(cnt)