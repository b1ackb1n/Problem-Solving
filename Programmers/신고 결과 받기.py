def solution(id_list, report, k):
    table = {id:[] for id in id_list}
    cnt = {id:0 for id in id_list}
    
    for re in report:
        user = re.split(' ')
        table[user[1]].append(user[0])

    for value in table.values():
        if len(set(value))>=k:
            for v in set(value):
                cnt[v]+=1

    return list(cnt.values())
