import sys
import statistics
from collections import Counter

N = int(sys.stdin.readline().strip())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline().strip()))
    
num_frq = Counter(num)
most_com = num_frq.most_common()
max_frq = most_com[0][1]
most_frq = []

for item, count in most_com:
    if max_frq == count:
        most_frq.append(item)
    else:
        break

print(round(statistics.mean(num)))
print(statistics.median(num))
if len(most_frq) == 1:
    print(most_frq[0])
else:
    print(sorted(most_frq)[1])
print(max(num)-min(num))
