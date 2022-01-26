import sys
sys.stdin = open('./input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cv = [list(map(int, input().split())) for _ in range(N)]
    cv.sort(key=lambda x: x[0])
    interview = [cv[i][1] for i in range(N)]

    res = 1
    grade = interview[0]

    for i in range(1, N):
        grade = min(grade, interview[i])
        if grade == interview[i]:
            res += 1
    print(res)
