def solution(s):
    answer = []
    s = s.replace('{{','').replace('}}','').split('},{')
    s.sort(key=len) # len기준 정렬
    for i in s:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer
