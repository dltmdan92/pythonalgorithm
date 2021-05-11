"""
실습과제
100XP
영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.

어느 날 문득, 호기심이 생겼습니다. 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?

계단 4개를 올라간다고 가정하면, 이런 방법들이 있습니다.

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
총 5개 방법이 있네요.

함수 staircase는 파라미터로 계단 수 n을 받고, 올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴합니다.

print(staircase(0))  # => 1
print(staircase(1))  # => 1
print(staircase(4))  # => 5

피보나치 수열을 활용할 것!!!
--> 정답 참고 : 출근정답.py 고고고
"""

def staircase(n):
    # 코드를 작성하세요.
    div = n // 2
    total = 0

    # i는 2의 갯수
    for count_of_two in range(0, div + 1):
        count_of_one = n - (count_of_two * 2)

        max_boonja = count_of_one + count_of_two
        boonja = 1

        for i in range(1, max_boonja + 1):
            boonja *= i

        boonmo1 = 1

        for i in range(1, count_of_two + 1):
            boonmo1 *= i

        boonmo2 = 1

        for i in range(1, count_of_one + 1):
            boonmo2 *= i

        total += boonja // (boonmo1 * boonmo2)

    return total


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
