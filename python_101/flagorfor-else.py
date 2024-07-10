

def solution(int_list):
    product = 1
    for i in range(5):
        product *= int_list[i]
        if int(product**0.5)**2 == product:
            return "found"
    return "not found"


int_list = [int(input()) for _ in range(5)]

print(solution(int_list))
