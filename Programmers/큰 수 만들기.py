# 최종 풀이
def solution(number, k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
    return ''.join(answer)[:len(number)-k]



# 시간 초과: 33.3/100
from itertools import combinations
def solution(number, k):
    answer = []
    case = list(combinations(number, len(number)-k))
    for c in case:
        answer.append(''.join(c))
    return str(max(answer))


# miss edge case: 91.7/100
def solution(number, k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
    return ''.join(answer)
