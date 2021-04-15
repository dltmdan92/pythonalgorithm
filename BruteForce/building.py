"""
건물 사이사이 물 채우기
"""

def trapping_rain(buildings):
    # 코드를 작성하세요
    sum_val = 0

    for i in range(1, len(buildings) - 1):
        left_max = 0

        for l in range(0, i):
            if buildings[l] > left_max:
                left_max = buildings[l]

        right_max = 0

        for r in range(i + 1, len(buildings)):
            if buildings[r] > right_max:
                right_max = buildings[r]

        if left_max > right_max > buildings[i]:
            sum_val = sum_val + right_max - buildings[i]
        elif right_max > left_max > buildings[i]:
            sum_val = sum_val + left_max - buildings[i]

    return sum_val


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))