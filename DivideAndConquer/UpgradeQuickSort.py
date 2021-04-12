# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
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

# 퀵 정렬 (start, end 파라미터 없이도 호출이 가능하도록 수정해보세요!)
def quicksort(my_list, start = 0, end = None):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    if end == None:
        end = len(my_list) - 1
    if start < end:
        pivot_index = partition(my_list, start, end)
        quicksort(my_list, start, pivot_index - 1)
        quicksort(my_list, pivot_index + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)