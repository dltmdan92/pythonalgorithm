# 공간 최적화 코드
# 리스트나 딕셔너리를 쓰게 될 경우 O(n)
# 임시변수로만 사용할 경우 O(1)
def fib_optimized(n):
    # 코드를 작성하세요.
    current = 1
    previous = 0

    for i in range(1, n):
        temp = current
        current = current + previous
        previous = temp
        # current, previous = current + previous, current
        # 파이썬에서는 이렇게 임시변수를 안쓰고 한 라인에서 사용할 수 도 있다

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
