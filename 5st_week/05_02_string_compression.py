input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []  # 1~len까지 압축했을때 길이 값

    # 절반 이상으로 나누면 절대 2로 압축될수가없음
    # 갯수가 틀리면 애초에 다른값이기 때문에
    # 딱 절반 만큼만 나눠서 확인
    # 1부터 n//2 씩 나눠서 같은지 확인
    for split_size in range(1, n // 2 + 1):
        compressed = ""
        # string 갯수 단위로 쪼개기 *

        # [i:i + split_size] 이건
        # i부터 i + split_size 이 구간까지 내용을 가져오는것

        # split_size가 1일때
        # i는 0 , 1 , 2, 3 ,4 ,5, 6
        # 0~1 , 1,2 이런식으로 한글자씩 string 배열에 담음

        # split_size가 2일때
        # i는 0 , 1 , 2, 3 ,4 ,5, 6
        # 0~2 , 1~3 이런식으로 두글자씩 string 배열에 담음

        # split_size 만큼 반복해서 문자열 나누기 작업 진행 및 압축진행
        # 마지막에 배열에 해당 길이값들 저장해놓고 min함수로 최적의 값 리턴

        # 리스트 컴프리헨션(list comprehension) 문법
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        count = 1

        for j in range(0, len(splited) - 1):
            cur, next = splited[j], splited[j + 1]
            if cur == next:
                count += 1
            else:  # 이전 문자와 다르다면
                if count > 1:
                    compressed += (str(count) + cur)
                else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
                    compressed += cur
                count = 1  # 초기화

        # 마지막 문자열들은 위에 반복문에서 동작하지않기 때문에
        # 마지막으로 처리해줘야됨
        # count 1은 마지막값이 다를경우
        # 1이 아닌 그이상인 경우에는 같은값이기때문에 앞에서 숫자 카운트 + 문자열
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
            compressed += splited[-1]

        compression_length_array.append(len(compressed))

    # min 함수로 가장 낮은 값 리턴 (가장 압축률이 좋은 값)
    return min(compression_length_array)  # 최솟값 리턴

print(string_compression(input))

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
