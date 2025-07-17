def count_down(number):
    # return을 적절히 해주지 않으면 무한 호출됨
    if number < 0:
        return

    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)  # 59 -> 59 -> 58 ...


