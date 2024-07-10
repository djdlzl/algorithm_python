'''docstring'''

bandage = [1, 1, 1,]
health = 5
attacks = [[1, 2], [3, 2]]


def solution(bandage, health, attacks):
    playtime = 0
    lasttime = attacks[-1][0]

    for i in range(lasttime):
        if playtime == attacks[i][0]:
            health -= attacks[i][1]
        else:
            health += bandage[1]
            print(bandage)
        print(health)


print(solution(bandage, health, attacks))
