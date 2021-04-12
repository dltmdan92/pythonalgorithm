def min_fee(pages_to_print):
    # 코드를 작성하세요.
    i = 1
    while i < len(pages_to_print):
        j = i
        while j > 0:
            if pages_to_print[j] < pages_to_print[j - 1]:
                temp = pages_to_print[j]
                pages_to_print[j] = pages_to_print[j - 1]
                pages_to_print[j - 1] = temp
            j -= 1
        i += 1
    sum = 0
    for x in range(0, len(pages_to_print)):
        sum += (len(pages_to_print) - x) * pages_to_print[x]
    return sum


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
