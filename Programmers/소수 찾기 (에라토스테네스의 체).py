# 에라토스테네스의 체
def solution(n):
    num = set(range(2, n+1))
    for i in range (2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            # i가 num에 있으면 i를 제외한 i의 배수set를 지운다.
    return len(num)


# 정확성75 효율성12.5 (87.5/100)
'''
import math 
def isprime(num):
    if num<2: return False
    else:
        for i in range (2, int(math.sqrt(num))+1):
            if num%i==0: return False
        return True

def solution(n):
    answer = 0
    for i in range (2, n+1):
        if isprime(i): answer+=1
    return answer
'''
