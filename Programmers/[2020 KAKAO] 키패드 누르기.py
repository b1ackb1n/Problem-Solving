pad = {1:[0,0], 2:[0,1], 3:[0,2],
       4:[1,0], 5:[1,1], 6:[1,2],
       7:[2,0], 8:[2,1], 9:[2,2],
       '*':[3,0], 0:[3,1], '#':[3,2]}

def dist(n1, n2):
    return abs(pad[n1][0]-pad[n2][0])+abs(pad[n1][1]-pad[n2][1])

def solution(numbers, hand):
    answer = ''
    left, right = ['*'], ['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left.append(num)
        elif num in [3,6,9]:
            answer += 'R'
            right.append(num)
        else:
            if dist(num, left[-1]) < dist(num, right[-1]):
                answer += 'L'
                left.append(num)
            elif dist(num, left[-1]) > dist(num, right[-1]):
                answer += 'R'
                right.append(num)
            else:
                if hand == 'left':
                    answer += 'L'
                    left.append(num)
                else:
                    answer += 'R'
                    right.append(num)
    return answer
