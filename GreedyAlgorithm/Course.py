def course_selection(course_list):
    # 코드를 작성하세요.
    i = 1
    while i < len(course_list):
        j = i
        while j > 0:
            if course_list[j][1] < course_list[j - 1][1]:
                temp = course_list[j]
                course_list[j] = course_list[j - 1]
                course_list[j - 1] = temp
            j -= 1
        i += 1
    rst_list = [course_list[0]]
    for i in range(1, len(course_list)):
        if rst_list[len(rst_list) - 1][1] < course_list[i][0]:
            rst_list.append(course_list[i])
    return rst_list


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
