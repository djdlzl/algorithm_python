from itertools import permutations

list1 = [1, 2, 3]


def solution(mylist):
    answer = sorted(map(list, permutations(mylist)))
    print(answer)
    return answer


solution(list1)
