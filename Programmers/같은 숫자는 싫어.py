'''
def solution(arr):
    answer = []
    for i in range (len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
            if i==len(arr)-2: 
                answer.append(arr[i+1])
        else:
            if i==len(arr)-2: 
                answer.append(arr[i+1])
            continue
    return answer
'''

# Stack 이용한 풀이
# 가장 최근 값과 비교해서 다르면 넣고 같으면 생략
def solution(arr):
    answer = []
    for i in arr:
        if len(answer)>0 and answer[-1]==i:
            continue
        else: answer.append(i)
    return answer
