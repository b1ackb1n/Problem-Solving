def solution(n):
    n = list(str(n))
    #answer = sorted(n, reverse=True)
    n.reverse()
    return list(map(int, n))
