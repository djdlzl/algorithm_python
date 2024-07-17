from sys import stdin

S = stdin.readline().strip()
count = 0

base = S[0]

for i in range(1, len(S)):
    if S[i] != base and S[i-1] == base:
        count += 1

print(count)
