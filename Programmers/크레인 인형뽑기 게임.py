# 조건 재명시: board의 마지막 인덱스부터 바닥에 쌓인다.
def solution(board, moves):
    arr = []
    answer = 0
    
    for move in moves:
        for i in range (len(board)):
            if board[i][move-1]>0: #idx주의
                arr.append(board[i][move-1])
                board[i][move-1]=0
                
                if len(arr)>1: #연속된 수의 중복성 체크
                    if arr[-1]==arr[-2]:
                        arr.pop(-1)
                        arr.pop(-1)
                        answer += 2
                break
    
    return answer