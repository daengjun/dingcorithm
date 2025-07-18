input = [4, 6, 2, 9, 1]

# 0 1 2 3 4
# [4, 6, 2, 9, 1]
#
# 0 1 2 3
# [4, 6, 2, 9, 1]
#
# 0 1 2
# [4, 6, 2, 9, 1]
#
# 0 1
# [4, 6, 2, 9, 1]

# for i in range(5-1):
#     for j in range(5-i-1):
#         print(j)

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # print(i,j)
            if array[j] > array[j + 1]:
                 array[j] , array[j + 1] =  array[j+1] ,array[j]

    # 이 부분을 채워보세요!
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", bubble_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", bubble_sort([100, 56, -3, 32, 44]))
