import sys
sys.stdin = open('./input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    people.sort(key=lambda x: x[0])
    print(people)

    cnt = 1
    tmp = people[0][1]

    for i in range(N):
        if tmp > people[i][1]:
            cnt += 1
            tmp = people[i][1]

    print(cnt)

