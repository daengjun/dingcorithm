from collections import deque

balanced_parentheses_string = "()))((()"


# 순차적으로 구현하면 풀리는 문제
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
# 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
# 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
# 4-3. ')'를 다시 붙입니다.
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
# 4-5. 생성된 문자열을 반환합니다.


# 올바른 괄호인지 확인하는 함수
# stack 사용해서 "(" 값을 하나씩 꺼내서
# 마지막에 stack 갯수가 0개라면 올바른 괄호라고 볼수있음
def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


def separate_to_u_v(string):  # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    # 균형 잡힌 괄호 u에 넣기
    while queue:  # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    # 나머지 v에 담기
    v = ''.join(list(queue))
    return u, v


# 괄호의 서로 반대값으로 뒤집기
# ")" -> "(" , "(" -> ")"
def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def change_to_correct_parentheses(string):
    # 1번 빈값이면 바로 리턴
    if string == '':
        return ''
    u, v = separate_to_u_v(string)  # 2번
    if is_correct_parentheses(u):  # 3번
        return u + change_to_correct_parentheses(v)
    else:  # 4번 괄호 씌우기
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
