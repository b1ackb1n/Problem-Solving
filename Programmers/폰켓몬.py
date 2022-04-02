def solution(nums):
    nunique = len(set(nums))
    nchoice = len(nums)//2
    return min(nunique, nchoice)

'''''
# 시간 초과 풀이
from itertools import combinations
def solution(nums):
    answer = 0
    case = list(combinations(nums, len(nums)//2))
    for i in case:
        if answer<len(set(i)):
            answer = len(set(i))
    return answer
'''''
