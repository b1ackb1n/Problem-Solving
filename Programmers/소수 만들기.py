import math
from itertools import combinations

def isprime(n):
    if n<2: return False
    else:
        for i in range (2, int(math.sqrt(n)+1)):
            if n%i==0: return False
        return True

def solution(nums):
    answer = 0
    tmp = []
    cases = list(combinations(nums, 3))
    for case in cases:
        tmp.append(sum(case))
    for t in tmp:
        if isprime(t): answer+=1
            
    return answer
