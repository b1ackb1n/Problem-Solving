'''
# 시간초과 26.7/100
from itertools import permutations
def solution(numbers):
    answer = ''
    arr, nums = [], []
    tmp = list(permutations(numbers))
    for t in tmp:
        arr.append(list(map(str, t)))
    print(arr)
    
    for a in arr:
        nums.append(int(''.join(a)))

    return str(sorted(nums)[-1])
'''

def solution(numbers):
    answer=''
    n = list(map(str, numbers))
    n.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(n)))
    return answer
