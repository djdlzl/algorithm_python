from sys import stdin
from collections import Counter

num_list = list(map(int, list(stdin.readline().strip())))
num_dict = Counter(num_list)
num_select = min(num_dict, key=num_dict.get)
count = 0

for i in range(len(num_list)):
    if i < (len(num_list)-1):
        if num_list[i] != num_list[i+1] and num_list[i] == num_select:
            count += 1

print(count)
