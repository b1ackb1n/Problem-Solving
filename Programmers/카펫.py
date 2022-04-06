def solution(brown, yellow):
    answer = []
    for i in range (1, yellow+1):
        if yellow%i==0:
            y_w, y_h = yellow//i, i
            if y_w*2 + y_h*2 + 4 == brown:
                answer.append(y_w+2)
                answer.append(y_h+2)
                break
    return sorted(answer, reverse=True)
