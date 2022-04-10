def solution(citations):
    citations.sort()
    for i in range (len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0 #논문이 한번도 인용되지 않은 경우

'''''
def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for idx, citation in enumerate(citations):
        if idx >= citation: #논문수>=인용횟수
            return idx
    return len(citations)

# 87.5/100
def solution(citations):
    answer=0
    citations.sort()
    for i in range (len(citations)):
        cnt=0
        for c in citations:
            if c>=i: cnt+=1
        if i==cnt: answer=cnt
    return answer
'''''
