"""
실습과제
100XP
이미 sublist_max 함수를 각각 Brute Force과 Divide and Conquer 방식으로 작성했는데요.
Brute Force로 풀었을 때는 시간 복잡도가 O(n^2), Divide and Conquer를 사용했을 때는 O(nlgn)였습니다.

이번 과제에서는 시간 복잡도를 O(n)로 한 번 더 단축해보세요!

과제 설명은 저번 챕터를 참고하세요!
"""

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