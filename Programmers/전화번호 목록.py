def solution(phone_book):
    phone_book.sort()
    for i in range (len(phone_book)-1):
        if(phone_book[i]==phone_book[i+1][:len(phone_book[i])]):
            return False
    return True

'''
len(ith)까지만 비교하기!
index out of range
'''
