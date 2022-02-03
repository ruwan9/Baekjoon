import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs():
    queue = deque()
    queue.append((1, 0))
    arr[1][0] = 0

    while queue:
        s, c = queue.popleft()
        if arr[s][s] == -1:
            arr[s][s] = arr[s][c] + 1
            queue.append((s, s))
        if s+c <= S and arr[s+c][c] == -1:
            arr[s+c][c] = arr[s][c] + 1
            queue.append((s+c, c))
        if s-1 >= 0 and arr[s-1][c] == -1:
            arr[s-1][c] = arr[s][c] + 1
            queue.append((s-1, c))


S = int(input())
arr = [[-1] * (S+1) for _ in range(S+1)]
bfs()
print(arr)
ans = arr[S][1]
for i in range(1, S):
    if arr[S][i] != -1:
        ans = min(ans, arr[S][i])

print(ans)