for _ in range (int(input())):
    n = int(input())
    answer = ''
    
    while (n>0):
        answer = str(n%2) + answer
        n = n//2

    for idx, val in enumerate (answer[::-1]):
        if val == '1':
            print(idx, end=' ')


'''
### 파이썬 진수변환 내장 함수
for _ in range (int(input())):
    num = bin(int(input)))[:2] # 숫자만 slicing
    for i in range (len(num)):
        if num[-i-1]=='1': # 리스트 거꾸로 순회할 때 [-i-1]
            print(i, end=' ') # 출력문 end
'''
