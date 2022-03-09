def solution(board, moves):
    arr = []
    cnt = 0
    for i in range (len(moves)):
        arr.append(board[moves[i]-1].pop())
    for a in arr:
        if a==0: arr.remove(a)
    
    for i in range (0, len(arr)-1, 2):
        if arr[i]==arr[i+1]: cnt+=2
        
    return cnt
