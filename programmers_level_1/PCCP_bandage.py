'''docstring'''


def solution(bandage, health, attacks):
    play_time = 0
    last_time = attacks[-1][0]
    attacks_time = [t for t, d in attacks]
    attacks_search = 0
    success_count = 0
    max_health = health

    while play_time <= last_time:

        print(f'시간:{play_time}')

        # 첫턴 넘기기
        if play_time == 0:
            play_time += 1
            continue
        # 몬스터 공격
        elif play_time in attacks_time:
            health -= attacks[attacks_search][1]
            attacks_search += 1
            success_count = 0
            print('몬스터 공격!')
        # 체력 회복
        else:
            # 추가 회복
            success_count += 1
            if success_count == bandage[0]:
                health += bandage[1] + bandage[2]
                success_count = 0
                print('추가 체력 회복')
            # 회복
            else:
                health += bandage[1]
                print('체력 회복!')

        # 체력이 0이하면 -1 리턴
        if health <= 0:
            print('몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다.')
            return -1
        if health > max_health:
            health = max_health
            print('최대 체력 이상의 체력을 가질 수 없습니다.')
        print(f'현재체력:{health}')
        play_time += 1
        if play_time > last_time:
            return health


bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bandage, health, attacks))
