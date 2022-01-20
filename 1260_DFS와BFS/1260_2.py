import sys
sys.stdin = open('../inputs/1260.txt')
from collections import deque


def bfs(start_v):
  queue = deque()
  discoverd = [start_v]
  queue.append(start_v)

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for w in range(len(graph[start_v])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        queue.append(w)


def dfs(start_v, discoverd=[]):
  discoverd.append(start_v)
  print(start_v, end=' ')

  for w in range(len(graph[start_v])):
    if graph[start_v][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
# print(graph)
for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1
print(graph)

dfs(V)
print()
bfs(V)