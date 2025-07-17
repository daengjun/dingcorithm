input = "abcba"


# 재귀 함수는 문제의 범위를 조금씩 좁혀나감

# v   v
#  v v
#   v

# abcba

# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):  # i: 0 ~ n-1
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True


# 재귀 함수
def is_palindrome(string):
    if string[0] != string[-1]:
        return False

    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])


print(is_palindrome(input))
