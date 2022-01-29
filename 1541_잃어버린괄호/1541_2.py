import sys
sys.stdin = open('input.txt')

equ = input().split('-')

nums = []
for i in equ:
    tmp = 0
    b = i.split('+')
    for j in b:
        tmp += int(j)
    nums.append(tmp)

ans = nums[0]
for n in range(1, len(nums)):
    ans -= nums[n]

print(ans)