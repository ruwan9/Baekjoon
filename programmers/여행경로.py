from collections import deque
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]

def solution(tickets):
    tickets.sort(key=lambda x: x[1])  # 경로 알파벳 순서로 정렬
    print(tickets)
    answer = []
    queue = deque()
    queue.append(('ICN'))  # 처음 시작점은 항상 인천
    visited = [0] * len(tickets)  # 방문처리

    # bfs
    while queue:
        v = queue.popleft()
        answer.append(v)

        for i in range(len(tickets)):
            if v in tickets[i] and visited[i] == 0:
                queue.append(tickets[i][1])
                visited[i] = 1

    return answer

print(solution(tickets))