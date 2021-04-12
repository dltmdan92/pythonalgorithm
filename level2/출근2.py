# 높이 n개의 계단을 올라가는 방법을 리턴한다
# n(4) = n(4 - possible_steps[0]) + n(4 - possible_steps[1]) + n(4 - possible_steps[2])
# tabulation으로 풀어라
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    # 계단 높이가 0 이거나 1 이면 올라가는 방법은 한 가지밖에 없다.
    number_of_ways = [1, 1]

    # 이 변수들을 업데이트 해주며 n 번째 계단을 오르는 방법의 수를 구한다.
    for height in range(2, stairs + 1):
        number_of_ways.append(0)

        for step in possible_steps:
            if height - step >= 0:
                number_of_ways[height] += number_of_ways[height - step]

    return number_of_ways[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))