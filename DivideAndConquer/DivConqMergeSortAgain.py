"""
TODO Divide and Conquer 방식으로 merge_sort 함수를 써 보세요. merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴합니다.
"""

def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
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

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    mid = len(my_list) // 2

    if len(my_list) < 2:
        return my_list

    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
