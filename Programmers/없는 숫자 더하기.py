def solution(numbers):
    num = [1,2,3,4,5,6,7,8,9]
    for n in numbers:
        if n in num:
            num.remove(n)
    return sum(num)
