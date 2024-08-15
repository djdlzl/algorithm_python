room = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]
r = 1
c = 1
Dir = 3

upper = room[r-1][c]
right = room[r][c+1]
down = room[r+1][c]
left = room[r][c-1]

dir_map = {0: upper, 1: right, 2: down, 3: left}

print(dir_map[Dir])
