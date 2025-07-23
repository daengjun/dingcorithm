all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# 1. 2중 반복문 입니다.
# for student in all_students:
#     # 반복
#     is_present = False
#     for present_students in present_students:
#         if student == present_students:
#             is_present = True
#     if not is_present:
#         return student

# 2. 정렬
# 정렬 이후에 하나하나 원소들을 보면서 존재하지 않는 학생을 찾으면 결석한 친구를 찾을 수 있음

# 3. Dictionary , Hash table
# all_students 들을 돌면서 , hash table의 키값에 해당 학생들을 등록한다.
# present_students 을 돌면서 hash talbe의 키값을 제거한다.
# 그리고 나서 남아있는 hash table의 키 값에 해당하는 학생이 결석한 학생이다.


def get_absent_student(all_array, present_array):
    dict = {}
    for student in all_array:
        dict[student] = True

    for present_student in present_array:
        del dict[present_student]

    for key in dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ", get_absent_student(["류진", "예지", "채령", "리아", "유나"], ["리아", "류진", "채령", "유나"]))
print("정답 = RM / 현재 풀이 값 = ", get_absent_student(["정국", "진", "뷔", "슈가", "지민", "RM"], ["뷔", "정국", "지민", "진", "슈가"]))
