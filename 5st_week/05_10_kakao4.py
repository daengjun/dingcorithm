import re
from itertools import permutations

def solution(expression):
    answer = 0

    # 연산자 뽑기
    operation_list = list()
    if '*' in expression:
        operation_list.append('*')
    if '+' in expression:
        operation_list.append('+')
    if '-' in expression:
        operation_list.append('-')

    # 연산자 경우의수 뽑기
    operation_permutations = list(permutations(operation_list))

    # 정규식으로 나누기
    # ["3","+","2"+"*"]
    expression = re.split('([^0-9])', expression)

    # 연산자 경우의수 배열리스트에서 한 인덱스씩 빼서 값 계산
    for operation_permutation in operation_permutations:
        # 배열 얕은 복사
        copied_expression = expression[:]


        for operator in operation_permutation:
            # 연산자가 없을때까지
            while operator in copied_expression:
                op_idx = copied_expression.index(operator)
                cal = str(
                    eval(copied_expression[op_idx - 1] + copied_expression[op_idx] + copied_expression[op_idx + 1])
                )

                copied_expression[op_idx - 1] = cal
                copied_expression = copied_expression[:op_idx] + copied_expression[op_idx + 2:]

        answer = max(answer, abs((int(copied_expression[0]))))

    return answer