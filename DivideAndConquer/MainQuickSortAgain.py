"""
Divide and Conquer 방식으로 quicksort 함수를 써 보세요.
quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 범위를 나타내는 인덱스 start와 인덱스 end를 받습니다.

merge_sort 함수와 달리 quicksort 함수는 정렬된 새로운 리스트를 리턴하는 게 아니라,
파라미터로 받는 리스트 자체를 정렬시키는 것입니다.
"""

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    big_area_index = start
    index = start
    pivot = my_list[end]

    while index < end:
        # 현재 탐색 데이터가 피벗 보다 큰 경우 (big_area) 아무 액션 X
        #if my_list[index] > pivot:
            # big_area는 현위치
        # 현재 탐색 데이터가 피벗 보다 작은 경우 -> 앞에 있는 big_area와 스왑
        if my_list[index] <= pivot:
            # big_area와 스왑하고
            if index != big_area_index:
                swap_elements(my_list, index, big_area_index)
            # big_area도 다음으로
            big_area_index += 1
        # 다음 인덱스로
        index += 1

    # 피벗과 big_area_index와 스왑
    swap_elements(my_list, big_area_index, end)
    return big_area_index

# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    if end is None:
        end = len(my_list) - 1
    # 코드를 작성하세요.
    if start >= end:
        return
    pivot_index = partition(my_list, start, end)
    quicksort(my_list, start, pivot_index - 1)
    quicksort(my_list, pivot_index + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)