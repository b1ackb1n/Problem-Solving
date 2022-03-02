import math
def solution(n):
    if math.sqrt(n) == int(n**0.5):
        return (math.sqrt(n)+1)**2
    else: return -1
