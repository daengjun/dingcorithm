input = 20

# 20은 값이 잘나오지만
# 100이상 입력할경우 연산결과가 너무 길어서
# 정상적인 값 표시 x
def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765
