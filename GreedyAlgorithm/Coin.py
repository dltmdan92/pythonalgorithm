def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    # 코인리스트 금액 큰 순으로 sorting
    i = 1
    while i < len(coin_list):
        j = i
        while j > 0:
            if coin_list[j] > coin_list[j - 1]:
                temp = coin_list[j]
                coin_list[j] = coin_list[j - 1]
                coin_list[j - 1] = temp
            j -= 1
        i += 1

    sum = 0
    for i in coin_list:
        cnt = value // i
        sum += cnt
        value %= i
    return sum



# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))