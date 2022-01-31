def solution(s):
    answer=[]
    
    if len(s)==1: return 1
    for n in range (1, len(s)//2+1):
        cnt=1
        res= ''
        tmp=s[:n]
        for i in range (n, len(s)+n, n):
            if tmp == s[i:i+n]:
                cnt+=1
            else:
                if cnt==1: res += tmp
                else: 
                    res += str(cnt)+tmp
                tmp = s[i:i+n] #비교군 갱신, move to next str
                cnt=1
        answer.append(len(res))
    return min(answer)
