def solution(N, stages):
    num = len(stages)
    table = {}

    for i in range (1, N+1):
        if num!=0:
            table[i] = stages.count(i)/num
            num -= stages.count(i)
        else:
            table[i] = 0

    return sorted(table, key=lambda x:table[x], reverse=True)

'''
Original: 정말 아무생각 없이 슥슥 짠 코드...
def solution(N, stages):
    answer = []
    table = {id:0 for id in range(1,N+1)}

    for i in range (1, N+1):
        mom, son, check = 0, 0, 0
        for s in stages:
            if s==i:
                mom+=1
                son+=1
            elif s>i: mom+=1
            elif s<i: check+=1
        if check==len(stages): table[i]=0
        else: table[i] = son/mom
        
    table = sorted(table.items(), key=lambda x:x[1], reverse=True)
    for t in table:
        answer.append(t[0])
        
    return answer
'''
