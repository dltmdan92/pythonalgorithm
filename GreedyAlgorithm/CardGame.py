def max_product(card_lists):
    # 코드를 작성하세요.
    # insertion sort를 사용해서 큰 것부터 내림차순으로 정렬
    for sub_list in card_lists:
        i = 1
        while i < len(sub_list):
            j = i
            while j > 0:
                if sub_list[j] > sub_list[j - 1]:
                    temp = sub_list[j]
                    sub_list[j] = sub_list[j - 1]
                    sub_list[j - 1] = temp
                j -= 1
            i += 1

    product = 1
    for list in card_lists:
        product *= list[0]

    return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
