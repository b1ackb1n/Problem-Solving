from fractions import gcd
def solution(a, b):
    g = gcd(a,b)
    l = (a*b)//g
    return [g,l]

'''
def solution(n, m):
    answer = []
    if n>m: (n,m)=(m,n)
    
    for i in range (1, m):
        if n%i==0 and m%i==0:
            maxi = i
    answer.append(maxi)
    
    for j in range (1, m+1):
        if (n*j)%m==0:
            answer.append(n*j)
            break
    return answer
'''
