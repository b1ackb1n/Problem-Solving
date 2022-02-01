n = int(input())
answer=''
while(n):
    if n%2:
        answer += '4'
        n //= 2
    else:
        answer += '7'
        n = n//2 - 1
return answer[::-1]
