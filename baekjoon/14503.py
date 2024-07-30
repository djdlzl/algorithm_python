import sys

First = list(int(sys.stdin.readline().strip()))
Second = list(int(sys.stdin.readline().strip()))

N = First[0]
M = First[1]
r = Second[0]
c = Second[1]
Dir = Second[2]
room = []

for _ in range(len(N)):
    room.append(list(int(sys.stdin.readline().strip())))
