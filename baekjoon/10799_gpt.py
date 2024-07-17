from sys import stdin

brakets = stdin.readline().strip()
stack = []
count = 0

for i, char in enumerate(brakets):
    if char == '(':
        stack.append(i)
    else:
        if stack[-1] == i - 1:
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
