import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
people = list(input() for _ in range(N+M))
h = people[:N]
s = people[N:]
res = []

for person in h:
    if person in s:
        res.append(person)

res.sort()
print(len(res))
for i in res:
    print(i)