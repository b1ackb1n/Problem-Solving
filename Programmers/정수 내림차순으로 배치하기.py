def solution(n):
    answer = ''
    ls = list(str(int(n)))
    ls.sort(reverse=True)
    return int(''.join(ls))
