from collections import Counter
def solution(participant, completion):
    answer = list((Counter(participant)-Counter(completion)).keys())[0]
    return answer
