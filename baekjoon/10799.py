from sys import stdin

input = list(stdin.readline().strip())
count_pipe = 0
count_piece = 0


for i in range(len(input)-1):
    if input[i] == '(' and input[i+1] != ')':
        count_pipe += 1
    elif input[i] == '(' and input[i+1] == ')':
        count_piece += count_pipe
    elif input[i] == ')' and input[i+1] == ')':
        count_piece += 1
        count_pipe -= 1

print(count_piece)
