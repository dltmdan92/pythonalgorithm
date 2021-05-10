"""
partition 함수는 리스트 my_list,
그리고 partition할 범위를 나타내는 인덱스 start와 인덱스 end를 파라미터로 받습니다.

my_list의 값들을 pivot 기준으로 재배치한 후,
pivot의 최종 위치 인덱스를 리턴해야 합니다.
"""

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    if start >= end:
        return my_list[end]

    big_area_index = start
    index = start
    pivot = my_list[end]

    while index < end:
        # 현재 탐색 데이터가 피벗 보다 큰 경우 (big_area)
        if my_list[index] > pivot:
            # big_area는 현위치
            # index는 다음 인덱스로
            index += 1
        # 현재 탐색 데이터가 피벗 보다 작은 경우 -> 앞에 있는 big_area와 스왑
        elif my_list[index] <= pivot:
            # big_area와 스왑하고
            if index != big_area_index:
                swap_elements(my_list, index, big_area_index)
            # 다음 인덱스로
            index += 1
            # big_area도 다음으로
            big_area_index += 1
    # 피벗과 big_area_index와 스왑
    swap_elements(my_list, big_area_index, end)

    #partition(my_list, start, big_area_index - 1)
    #partition(my_list, big_area_index + 1, end)
    return big_area_index

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
