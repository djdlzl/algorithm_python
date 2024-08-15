import sys
# 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def cleanBlock(r, c):
    if room[r][c] == 0:
        global count
        count += 1
        room[r][c] = 1


def checkRoute(r, c, Dir):

    check = 0
    upper = room[r-1][c]
    right = room[r][c+1]
    down = room[r+1][c]
    left = room[r][c-1]

    dir_map = {0: upper, 1: right, 2: down, 3: left}

    while True:
        cleanBlock(r, c)
        if Dir in dir_map:
            if all(x == 1 for x in (upper, right, down, left)):
                try:
                    r -= dx[Dir]
                    c -= dy[Dir]
                    check = room[r][c]
                except:
                    return
            else:
                while True:
                    if Dir == 0:
                        Dir = 3
                    else:
                        Dir -= 1
                    if dir_map[Dir]:  # Dir 방향이 1이면
                        continue
                    else:
                        break
                r += dx[Dir]
                c += dy[Dir]


First = list(map(int, sys.stdin.readline().strip().split(' ')))  # 방 크기
# 로봇청소기 좌표 + 방향
Second = list(map(int, sys.stdin.readline().strip().split(' ')))

N = First[0]
M = First[1]
r = Second[0]
c = Second[1]
Dir = Second[2]  # 방향
room = []
count = 0

for _ in range(N):  # 방 구조
    room.append(list(map(int, sys.stdin.readline().split(' '))))

if __name__ == '__main__':

    checkRoute(r, c, Dir)
    print(count)


# count = 0  # 방향전환용 count
# while dir_map[Dir] == 0:
#     Dir +=
# else:  # 0일 경우
#     if Dir == 0:
#         Dir = 3
#         count += 1
#     else:
#         Dir -= 1
#         count += 1
#     if count == 4:
#         break
