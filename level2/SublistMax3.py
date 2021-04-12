# O(n)으로 풀어보기
def sublist_max(profits):
    # 코드를 작성하세요.
    sum_max = profits[0]
    part_sum_max = profits[0]

    for i in range(1, len(profits)):
        part_sum_max = max(profits[i], profits[i] + part_sum_max)
        sum_max = max(sum_max, part_sum_max)
    return sum_max


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))