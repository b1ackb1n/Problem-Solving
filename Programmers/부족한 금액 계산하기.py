def solution(price, money, count):
    answer = 0
    for i in range (count):
        answer += price*(i+1)
    if answer-money<=0: return 0
    else: return answer-money
