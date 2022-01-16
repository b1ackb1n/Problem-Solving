def solution(answers):
    answer = []
    score = [0]*3
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range (len(answers)):
        if answers[i]==one[i%5]:
            score[0] += 1
        if answers[i]==two[i%8]:
            score[1] += 1
        if answers[i]==three[i%10]:
            score[2] += 1
    
    for i in range (len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    return answer
