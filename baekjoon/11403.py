import sys

line = int(sys.stdin.readline().rstrip('\n'))

G = [list(map(int, sys.stdin.readline().split())) for _ in range(line)]


def floyd_warshal(G):
    G_length = len(G)
    for k in range(G_length):
        for i in range(G_length):
            for j in range(G_length):
                if G[i][k] and G[k][j]:
                    G[i][j] = 1


floyd_warshal(G)

for row in G:
    print(*row)
