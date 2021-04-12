# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    #length = len(str(n))

    #if length == 1:
    #    return n
    #return int(str(n)[length - 1:length]) + sum_digits(int(str(n)[:length - 1]))
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))