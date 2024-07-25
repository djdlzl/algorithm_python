from sys import stdin


def is_VPS(VPS):
    stack = 0
    for char in VPS:
        if stack >= 0:
            if char == '(':
                stack += 1
            else:
                stack -= 1
    if stack == 0:
        return "YES"
    else:
        return "NO"


input = int(stdin.readline())
VPS = []

for _ in range(input):
    VPS.append(list(stdin.readline().strip('\n')))

for i in VPS:
    print(is_VPS(i))
