import sys
while True:
    stk = []
    ps = sys.stdin.readline().rstrip()
    
    if ps=='.': break
    for p in ps:
        if p=='(' or p=='[':
            stk.append(p)
        elif p==')':
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            else:
                stk.append(')')
                break
        elif p==']':
            if len(stk)!=0 and stk[-1]=='[':
                stk.pop()
            else:
                stk.append(']')
                break

    if len(stk)==0: print('yes')
    else: print('no')
