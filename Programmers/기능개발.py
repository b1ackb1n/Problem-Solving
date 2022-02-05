'''
# math.ceil 이용한 풀이
import math
def solution(progresses, speeds):
    n = math.ceil((100-progresses[0])/speeds[0])
    cnt = 1
    answer = []
    for i in range (1, len(speeds)):
        if progresses[i]+speeds[i]*n >= 100:
            cnt += 1
        else:
            answer.append(cnt)
            n = math.ceil((100-progresses[i])/speeds[i])
            cnt = 1
    answer.append(cnt) #이걸 빼먹었다..
    return answer
'''

# queue를 이용한 풀이
import math
def solution(progresses, speeds):
    time, cnt = 0, 0
    answer = []
    while len(progresses)>0:
        if progresses[0]+speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            if cnt>0: 
                answer.append(cnt)
                cnt=0
            time+=1
            
    answer.append(cnt)
    return answer
