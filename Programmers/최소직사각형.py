def solution(sizes):
    for i in sizes:
        i.sort(reverse=True)
    max_x = sorted(sizes, key=lambda x:x[0], reverse=True)[0][0]
    max_y = sorted(sizes, key=lambda x:x[1], reverse=True)[0][1]
    return max_x*max_y
