import sys
n = int(sys.stdin.readline())
stack = []

for _ in range (n):
    input = sys.stdin.readline().split()
    order = input[0]
    
    if order=='push':
        stack.append(input[1])
        
    elif order=='pop':
        if len(stack)==0: print(-1)
        else: print(stack.pop())
        
    elif order=='size':
        print(len(stack))
        
    elif order=='empty':
        if len(stack)==0: print(1)
        else: print(0)
        
    elif order=='top':
        if len(stack)==0: print(-1)
        else: print(stack[-1])
