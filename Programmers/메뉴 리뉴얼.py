from itertools import combinations
def solution(orders, course):
    answer = []
    table = {}
    for ord in orders:
        for cor in course:
            if len(ord) >= cor:
                tmp = list(combinations(ord, cor))
                for t in tmp:
                    menu = ''.join(sorted(t))
                    if menu not in table.keys():
                        table[menu] = 1
                    else:
                        table[menu] += 1

    temp = sorted(table.items(), key=lambda x:(-x[1], x[0]))
    temp = sorted(temp, key=lambda x:len(x[0]))
    
    a, b = len(temp[0][0]), temp[0][1]
    for t in temp:
        if len(t[0])>a:
            a, b = len(t[0]), t[1]
        if (t[1]>=b and t[1]>=2): # 메뉴는 최소 2개 이상
            answer.append(t[0])
        
    return sorted(answer)
