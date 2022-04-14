def solution(s):
    stk = []
    for i in s:
        if i=='(':
            stk.append(i)
        else:
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            else:
                stk.append(')')
                
    if len(stk) != 0:
        return False
    return True
