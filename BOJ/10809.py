s = input()
answer = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    if i in s:
        answer.append(s.find(i))
    else:
        answer.append(-1)
print(*answer)
