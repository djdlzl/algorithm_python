import sys
sys.setrecursionlimit(10**6)


def draw_stars(n):
    if n == 1:
        return ['*']

    stars = draw_stars(n//3)
    tmp = []

    for i in stars:
        tmp.append(i*3)
    for i in stars:
        tmp.append(i+' '*(n//3)+i)
    for i in stars:
        tmp.append(i*3)
    return tmp


N = int(sys.stdin.readline().strip())
print("\n".join(draw_stars(N)))
