from sys import stdin


def rec_count(qt, n, i, j):
    base = qt[0][0]
    for a in range(i):
        for b in range(j):
            if qt[i][j] == base:
                return base
            else:
                sub_quad_tree = [list() for _ in range(n**0.5)]
                rec_count()


N = int(stdin.readline())
quad_tree = [list(map(int, stdin.readline().strip('\n'))) for _ in range(N)]
