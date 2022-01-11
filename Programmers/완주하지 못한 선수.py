from collections import Counter
def solution(participant, completion):
    answer = list((Counter(participant)-Counter(completion)).keys())[0]
    return answer
'''
* 1명만 완주 못함: len(p)-len(c)=1, p-c=미완주자
* 참가자 중 동명이인 존재 (Hash)
* from collections import Counter
* Counter: 정렬 기반 딕셔너리 확장 {key:#key}
'''
