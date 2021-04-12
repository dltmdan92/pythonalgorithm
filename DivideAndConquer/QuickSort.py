# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp



# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    p_index = end
    big_index = start
    unknown_index = start

    while big_index < p_index and unknown_index < p_index:
        if my_list[p_index] < my_list[unknown_index]:
            unknown_index += 1
        elif my_list[p_index] >= my_list[unknown_index]:
            swap_elements(my_list, big_index, unknown_index)
            big_index += 1
            unknown_index += 1
    swap_elements(my_list, big_index, p_index)
    return big_index


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
