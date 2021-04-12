def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    max_result = 0
    for x in left_cards:
        for y in right_cards:
            if x * y >= max_result:
                max_result = x * y
    return max_result

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))