"""
Brute Force
모든 경우의 수를 탐색해서 최적의 값을 구해낸다.

결과는 구해내지만, 가장 비효율적인 방법이기도 하다.

장점
1. 직관적이고 명확하다
2. 답을 확실하게 찾을 수 있다.

모든 알고리즘의 시작은 Brute Force로 부터!
Brute Force를 통해 먼저 초반 탐색을 한 후에, 알고리즘 풀이를 그려나간다!

"""

def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    max_result = 0
    for x in left_cards:
        for y in right_cards:
            if x * y >= max_result:
                max_result = x * y
    return max_result

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))