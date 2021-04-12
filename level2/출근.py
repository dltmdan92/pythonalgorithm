def staircase(n):
    # 코드를 작성하세요.
    factorial_cache = {}
    return staircase_calc(n, factorial_cache)


def staircase_calc(n, cache):
    sum = 0
    for i in range(0, n // 2 + 1):
        rem = n - i * 2
        if i not in cache:
            cache[i] = factorial(i)
        if rem not in cache:
            cache[rem] = factorial(rem)
        if i + rem not in cache:
            cache[i + rem] = factorial(i + rem)

        sum += cache[i + rem] // (cache[i] * cache[rem])
    return sum


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
