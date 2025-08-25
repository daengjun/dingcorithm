def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            # 일치하는 스택이 없으면 false
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        # 스택이 남아있으면 false
        return False
    else:
        # 스택이 없으면 true
        return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
