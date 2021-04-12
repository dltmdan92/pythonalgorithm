"""
'선형 탐색(Linear Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.
선형 탐색이란, 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.

파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요.
0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해 주면 됩니다.

element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.

<주의 사항>
element in some_list와 같이 in 키워드를 사용하는 건 안 됩니다.
선형 탐색에 대한 이해를 테스트하는 과제이기 때문에, 반드시 반복문을 사용해서 해결해 주셔야 합니다.

자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.
힌트를 최대한 보지 않고, 스스로의 힘으로 푸시는 것이 좋습니다. 만약 도저히 모르겠다면, 최소한의 힌트만 참고해주세요!

<정답>
0
None
2
1
4
"""


def linear_search(element, some_list):
    # 코드를 작성하세요.
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

