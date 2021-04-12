#팔린 드롬 찾기

"""
팔린드롬 문제 설명

"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다.
문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요.
is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.
"""

def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(len(word) // 2):
        if word[i] == word[len(word) - 1 - i]:
            continue
        else:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))