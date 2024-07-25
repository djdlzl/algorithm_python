
from sys import stdin


def compress(row, col, size):

    num = quad_tree[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            if num != quad_tree[i][j]:
                size //= 2
                print("(", end="")
                compress(row, col, size)
                compress(row, col+size, size)
                compress(row+size, col, size)
                compress(row+size, col+size, size)
                print(")", end="")
                return
    print(num, end="")
    return


N = int(stdin.readline())
quad_tree = [list(map(int, stdin.readline().strip('\n'))) for _ in range(N)]
compress(0, 0, N)
