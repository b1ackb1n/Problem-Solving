def solution(d, budget):
    answer = 0
    for di in sorted(d):
        if di<=budget:
            answer += 1
            budget -= di
    return answer
