def solution(n):
    answer = ''
    # 3진수 변환 내장함수 없음, while문으로 직접 구현
    while(n>0): # 3진법 변환
        answer = str(n%3) + answer
        n //= 3
    return int(answer[::-1], 3) # 뒤집어서 다시 10진법
