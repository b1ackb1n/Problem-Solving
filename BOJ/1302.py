n = int(input())
arr = {}
for _ in range (n):
    title = input()
    if title not in arr:
        arr[title] = 1
    else:
        arr[title] += 1

# value 내림차순, key 오름차순
arr = sorted(arr.items(), key=lambda x: (-x[1],x[0]))
print(arr[0][0])

'''
books = []
max_value = max(arr.values())
for idx, val in arr.items():
    if val == max_value:
        books.append(idx)
print(sorted(books)[0])
'''