## 25분 소요


def solution(bandage, health, attacks):
    answer = 0
    tt = 0
    real_health = health
    real_time = 0

    bandage_time = bandage[0]
    bandage_amount = bandage[1]
    bandage_plus_amount = bandage[2]

    for attack in attacks:
        attack_time = attack[0]
        attack_damage = attack[1]
        for _ in range(tt+1, attack_time, 1):

            real_time += 1

            ## 체력 회복 중
            if real_health < health:
                real_health += bandage_amount

                ## 회복시간을 채우면 추가 회복
                if real_time == bandage_time:
                    real_health += bandage_plus_amount
                    real_time = 0
                
                ## 최대체력보다 더 회복하면 최대체력으로 고정
                if real_health > health:
                    real_health = health
        
        real_health -= attack_damage
        real_time = 0
        if real_health <= 0:
            return -1

        tt = attack_time

    answer = real_health
    return answer