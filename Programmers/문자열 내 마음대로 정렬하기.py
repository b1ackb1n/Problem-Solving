def solution(strings, n):
    strings.sort()
    return strings.sort(key=lambda x:x[n])

# 람다에 두 조건을 걸어서 한 번에 해결하기
# return strings.sort(key=lambda x: (x[n], x))
