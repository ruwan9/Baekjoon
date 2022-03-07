from collections import deque
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]


def solution(tickets):
    tickets.sort(reverse=True)  # 역순 정렬
    answer = []

    dic = dict()
    # 출발: 도착 형식으로 딕셔너리
    for ticket in tickets:
        if ticket[0] in dic:
            dic[ticket[0]].append(ticket[1])
        else:
            dic[ticket[0]] = [ticket[1]]

    stack = ['ICN']  # 인천 출발

    while stack:
        tmp = stack[-1]  # 출발지
        if tmp not in dic or len(dic[tmp]) == 0:
            answer.append(stack.pop())
        else:
            # 이거때문에 value값 역순 정렬
            stack.append(dic[tmp].pop())

    return answer[::-1]  # 거꾸로


print(solution(tickets))