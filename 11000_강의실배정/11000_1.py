import sys
sys.stdin = open('input.txt')
import heapq

N = int(input())
lst = []
heap = []
for _ in range(N):
    S, T = map(int, input().split())
    lst.append([S, T])

lst.sort(key=lambda x: x[0])
print(lst)
heapq.heappush(heap, lst[0][1]) # 첫 강의 끝나는 시간
print(heap)

for i in range(1, N):
    if heap[0] > lst[i][0]:
        heapq.heappush(heap, lst[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lst[i][1])
    print(i, heap)

print(heap)