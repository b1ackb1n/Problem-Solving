def solution(clothes):
    answer = 1
    wear = {}
    for cloth in clothes:
        if cloth[1] in wear.keys():
            wear[cloth[1]].append(cloth[0])
        else:
            wear[cloth[1]] = [cloth[0]]

    for val in wear.values():
        answer *= (len(val)+1)
        
    return answer-1
