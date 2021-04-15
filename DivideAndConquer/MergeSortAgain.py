"""
TODO 정렬된 두 리스트 list1, list2를 받아서, 하나의 정렬된 리스트를 리턴합니다.
"""


def merge(list1, list2):
    # 코드를 작성하세요.
    result = []
    list1_idx = 0
    list2_idx = 0

    while list1_idx < len(list1) and list2_idx < len(list2):
        if list1[list1_idx] > list2[list2_idx]:
            result.append(list2[list2_idx])
            list2_idx += 1
        else:
            result.append(list1[list1_idx])
            list1_idx += 1

    result += list1[list1_idx:]
    result += list2[list2_idx:]

    return result


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
