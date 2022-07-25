def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities)
        for i in range (len(priorities)):
            if priorities[i] == max_num:
                answer += 1
                priorities[i] = 0
                max_num = max(priorities)
                
                if i == location:
                    return answer
