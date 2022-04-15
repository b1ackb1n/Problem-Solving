def separate(p):
    cnt = 0
    for i in range (len(p)):
        if p[i]=='(': cnt+=1
        else: cnt-=1
        if cnt==0:
            u, v = p[:i+1], p[i+1:]
            return u, v
            
def check(p):
    stk = []
    for i in p:
        if i=='(': stk.append(i)
        else:
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            else: stk.append(i)
    if not stk: return True
    else: return False
        
def solution(p):
    answer = ''
    if not len(p):
        return p
    else:
        u, v = separate(p)
        if check(u):
            return u+solution(v)
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            for i in u[1:-1]:
                if i=='(':
                    answer += ')'
                else:
                    answer += '('
    return answer
