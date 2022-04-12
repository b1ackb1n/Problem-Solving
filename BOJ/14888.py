# 완전탐색(순열)
from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))

# operator 생성
op = ['+', '-', '*', '//']
op_numbers = list(map(int, input().split()))
operator = []
for l in range (4):
    for m in range (op_numbers[l]):
        operator.append(op[l])

answer = []
case = list(set(permutations(operator, N-1)))
for c in case:
    tmp = numbers[0]
    for i in range (1, N):
        if c[i-1]=='+':
            tmp += numbers[i]
        elif c[i-1]=='-':
            tmp -= numbers[i]
        elif c[i-1]=='*':
            tmp *= numbers[i]
        elif c[i-1]=='//':
            tmp = int(tmp/numbers[i])
    answer.append(tmp)

print(max(answer))
print(min(answer))
