def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    result_stops = []
    prev_stop = 0

    for i in range(0, len(water_stops)):
        if water_stops[i] - prev_stop > capacity:
            result_stops.append(water_stops[i - 1])
            capacity -= water_stops[i - 1]
    result_stops.append(water_stops[len(water_stops) - 1])
    return result_stops


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))