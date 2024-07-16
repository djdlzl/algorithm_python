from collections import Counter
from sys import stdin

N = stdin.readline().strip()
N_list = list(map(int, stdin.readline().split()))
M = stdin.readline().strip()
M_list = list(map(int, stdin.readline().split()))

counter = Counter(N_list)
counter_list = [counter[i] for i in M_list]

print(*counter_list)
