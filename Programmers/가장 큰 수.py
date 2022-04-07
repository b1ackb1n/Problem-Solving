'''
# 시간초과 26.7/100
from itertools import permutations
def solution(numbers):
    answer = []
    tmp = list(permutations(numbers, len(numbers)))
    for i in tmp:
        answer.append(int(''.join(map(str, i))))
    return str(max(answer))
'''

def solution(numbers):
    answer=''
    n = list(map(str, numbers))
    n.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(n)))
    return answer
