import string
def solution(s, n):
    answer = ''
    small = string.ascii_lowercase
    big = string.ascii_uppercase
    
    for si in s:
        if si in small:
            idx = small.find(si) + n
            answer += small[idx%26]
        elif si in big:
            idx = big.find(si) + n
            answer += big[idx%26]
        else:
            answer += ' '
            
    return answer
