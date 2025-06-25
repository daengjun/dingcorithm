# def find_max_num(array):
#     maxNum = array[0]
#     for num in array:
#         if (num > maxNum):
#             maxNum = num
#     return maxNum

# def find_max_num(array):
#     max_num = array[0]
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num

# def find_max_num(array):
#     for number in array:
#         is_max_num = True
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False
#         if is_max_num:
#             return number
#
#
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))


# for x in [1,2,3,4]:
#     print(x)
#     if x == 4:
#         break
# else:
#     print("완료되었습니다.")

# input = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for n in range(2, number + 1):
#         for i in prime_list:
#             if i * i <= n and n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)


# 0에서 1을 마주쳤을때 뒤집는다 -> 전체를 0으로 만들기위한 작업
# 1에서 0을 마주쳤을때 뒤집는다 -> 전체를 1로 만들기 위한 작업

# input = "011110"
#
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     count_to_all_zero = 0
#     count_to_all_one = 0
#
#     if string[0] == '0':
#         count_to_all_one += 1
#     elif string[0] == '1':
#         count_to_all_zero += 1
#
#     for i in range(len(string) - 1):
#         if string[i] != string[i + 1]:
#             if string[i + 1] == '0':
#                 count_to_all_one += 1
#             if string[i + 1] == '1':
#                 count_to_all_zero += 1
#
#     return min(count_to_all_one, count_to_all_zero)
#
#
# result = find_count_to_turn_out_to_all_zero_or_all_one(input)
# print(result)

# 각 알파벳은 중복이여도 상관 x 걍입력만 되면됨
# 중간에 없는 알파벳이 있을수도있습니다 ? 이게 먼솔


def summarize_string(target_string):
    age = int(input("나이를 입력하세요: "))
    print("내년엔", age + 1, "살이 되겠네요!")

    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))