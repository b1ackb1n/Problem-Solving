def solution(record):
    answer = []
    db = {}
    for re in record:
        log = re.split(' ')
        if log[0]=='Enter':
            if log[1] in db.keys():
                db[log[1]].append(log[2])
            else:
                db[log[1]] = [log[2]]
        elif log[0]=='Change':
            db[log[1]].append(log[2])

    for re in record:
        log = re.split(' ')
        if log[0]=='Enter':
            answer.append(db[log[1]][-1]+'님이 들어왔습니다.')
        elif log[0]=='Leave':
            answer.append(db[log[1]][-1]+'님이 나갔습니다.')
            
    return answer
