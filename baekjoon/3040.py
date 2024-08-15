import sys
from itertools import combinations

num = []


for _ in range(9):
    num.append(sys.stdin.readline().rstrip('\n'))

for comb in combinations(num, 7):
    if sum(map(int, comb)) == 100:
        for correct in comb:
            print(correct)
