def solution(dartResult):
    answer = []
    temp = ''
    for i in dartResult:
        if i.isnumeric():
            temp+=i
        elif i=='S':
            temp = int(temp)**1
            answer.append(temp)
            temp=''
        elif i=='D':
            temp = int(temp)**2
            answer.append(temp)
            temp=''
        elif i=='T':
            temp = int(temp)**3
            answer.append(temp)
            temp=''
        elif i=='*':
            if len(answer)>1:
                answer[-1]*=2
                answer[-2]*=2
            else:
                answer[-1]*=2
        elif i=='#':
            answer[-1]*=(-1)    
    return sum(answer)
