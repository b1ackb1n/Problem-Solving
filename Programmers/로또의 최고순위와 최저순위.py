def solution(lottos, win_nums):
    answer = []
    hit=0
    cnt = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    
    for num in win_nums:
        if num in lottos:
            hit += 1
    
    return rank[hit+cnt], rank[hit]
