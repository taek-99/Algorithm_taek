import math



def solution(signals):
    answer = 0
    sum_nums = []
    rgb_list = []
    n = len(signals)

    for nums in signals:
        nn = sum(nums)
        sum_nums.append(nn)
        
        rgb = []
        for idx in range(3):
            for _ in range(nums[idx]):
                rgb.append(idx)
        
        rgb_list.append(rgb)

    gcd_num = sum_nums[0]

    def gcd(a, b):  ## 최소공배수 구하기  == 한사이클을 구하기 위함
        return a * b // math.gcd(a, b)

    for sum_num in sum_nums[1:]:
        gcd_num = gcd(gcd_num, sum_num)


    for i in range(gcd_num):  ## 한 사이클 안에 노란불 겹치는거 있나 확인
        aa = 0
        for idx in range(n):
            idx2 = i % len(rgb_list[idx])
            if rgb_list[idx][idx2] != 1:
                break
            else:
                aa += 1
        
        if aa == n:
            return i + 1

    answer = -1  ## 한사이클 안에 못만나면 평생 못만나니깐 -1 리턴
    return answer