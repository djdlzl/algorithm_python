from collections import Counter

my_str = input().strip()

char_count = Counter(my_str)
max_count = max(char_count.values())
most_common = sorted(
    [char for char, count in char_count.items() if count == max_count])
result = ''.join(most_common)

print(char_count)
