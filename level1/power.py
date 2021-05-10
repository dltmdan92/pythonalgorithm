"""
실습과제
거듭 제곱을 계산하는 함수 power를 작성하고 싶습니다.
power는 파라미터로 자연수 x와 자연수 y를 받고, x^y 를 리턴합니다.

가장 쉽게 생각할 수 있는 방법은 반복문으로 단순하게 xx를 yy번 곱해 주는 방법입니다.

이 알고리즘의 시간 복잡도는 O(y)인데요. O(lg(y))로 더 빠르게 할 수는 없을까요?

주의
return x ** y는 답이 아닙니다.
우리는 거듭 제곱을 구하는 원리를 파악하여 효율적인 ‘알고리즘’을 구현하고 싶은 것입니다.
"""

def power(x, y):
    # 코드를 작성하세요.
    if y == 0:
        return 1

    subresult = power(x, y // 2)

    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))