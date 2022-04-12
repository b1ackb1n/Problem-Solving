# sol1: Tree
def solution(numbers, target):
    leaves = [0]
    for num in numbers:
        temp = []
        for parent in leaves:
            temp.append(parent-num)
            temp.append(parent+num)
        leaves = temp
    return leaves.count(target)


# sol2: product - 카티션곱
from itertools import product
def solution(numbers, target):
    l = [(x,-x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
