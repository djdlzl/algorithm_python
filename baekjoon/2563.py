import sys

N = int(sys.stdin.readline().strip())
xy = []

for _ in range(N):
    xy.append(list(map(int,sys.stdin.readline().strip().split())))
    
for item in xy:
    if item[0]+10 