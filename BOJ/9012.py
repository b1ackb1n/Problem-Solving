# sol1) count
import sys
T = int(input())

for _ in range (T):
    cnt=0
    ps = sys.stdin.readline().strip()
    for p in ps:
        if p=='(': cnt+=1
        else: cnt-=1
        if cnt<0: break # cnt<0 예외처리

    if cnt==0: print('YES')
    else: print('NO')


'''
# sol2) stack
for _ in range (T):
    stk=[]
    ps = sys.stdin.readline().strip()
    for p in ps:
        if p=='(': stk.append(p)
        else:
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            else: stk.append(')')
    if len(stk)==0: print('YES')
    else: print('NO')
'''
