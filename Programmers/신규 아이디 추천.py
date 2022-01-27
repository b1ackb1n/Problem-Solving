def solution(new_id):
    new_id = new_id.lower() #1
    ban = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in range (len(ban)):
        new_id = new_id.replace(ban[i],'') #2
        
    while '..' in new_id: #3
        new_id = new_id.replace('..', '.')
        
    '''    
    # index out of range
    if (new_id[0]=='.')&(len(new_id)>1): #4
        new_id = new_id[1:]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    '''
    new_id = new_id.strip('.') #4 최적화

    if new_id=='': #5
        new_id += 'a'
        
    if len(new_id)>=16: #6
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    
    if len(new_id)<=2: #7
        word = new_id[-1]
        while(len(new_id)!=3):
            new_id += word

    return new_id
