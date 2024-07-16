from sys import stdin
from bisect import bisect_left, bisect_right

N = stdin.readline().strip()
N_list = list(map(int, stdin.readline().split()))
M = stdin.readline().strip()
M_list = list(map(int, stdin.readline().split()))

N_list.sort()


def count_num(N_list, M_list):
    return [bisect_right(N_list, M_list[i]) - bisect_left(N_list, M_list[i]) for i in range(len(M_list))]


count_list = count_num(N_list, M_list)
print(*count_list)
