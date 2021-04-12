"""
실습과제
‘이진 탐색(Binary Search)’ 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.
이진 탐색 알고리즘은 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 합니다.
정렬된 리스트가 아니면 이 알고리즘은 적용이 불가능합니다.

왜 이 알고리즘의 이름이 ‘이진 탐색’일까요? 1회 비교를 거칠 때마다 탐색 범위가 (대략) 절반으로 줄어들기 때문입니다.

"""


def binary_search(element, some_list):
    # 코드를 작성하세요.
    # 중간 인덱스 추출
    result = 0

    while len(some_list) >= 1:
        mid_idx = len(some_list) // 2

        # 왼쪽으로 탐색
        if some_list[mid_idx] > element:
            some_list = some_list[:mid_idx]
        # 오른쪽으로 탐색
        elif some_list[mid_idx] < element:
            some_list = some_list[mid_idx+1:]
            result = result + mid_idx + 1
        # 일치 케이스
        else:
            return mid_idx + result


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))