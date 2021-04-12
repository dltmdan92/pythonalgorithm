"""
재귀함수에는 치명적인 단점이 있다.

Call Stack : 해당 쓰레드에서 함수의 시작 지점을 저장하는 곳

함수의 호출이 많아지면, Call Stack에 쌓이는 함수 데이터가 가득차게 된다.
파이썬에서는 이러한 현상을 막기 위해, Call Stack에 쌓이는 Maximum 수치를 1001개로 제한한다.

"""

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(1001))