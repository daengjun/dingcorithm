k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 뒤로 후진
# IF문으로 if(d ==0): 이런식으로 표현 해도됨
# 규칙성을 찾고 아래 코드처럼 구현한것
def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    # 게임판 길이만큼
    n = len(game_map)

    # 처음 시작한것도 카운트이기때문에 1
    turn_count = 1

    # [[],[],[],[]],[[],[],[],[]],[[],[],[],[]]... 의 형태로 current_stacked_horse_map 2차원 배열 생성
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]

    # ======================================================
    for i in range(horse_count):
        # 좌표 , 방향 값 꺼내기
        r, c, d = horse_location_and_directions[i]

        # current_stacked_horse_map 2차원 배열에 값 넣기
        current_stacked_horse_map[r][c].append(i)
    # ======================================================

    # turn_count 값이 1000 이하일때까지 무한 반복
    while turn_count <= 1000:
        # 말의 갯수 만큼 반복 이동 (한턴)
        for horse_index in range(horse_count):
            n = len(game_map)

            # 방향값대로 한방향 이동
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            #  3) 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
            #  2가 파란색
            # 범위를 벗어나거나 , 파란색을 만났을때
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 전환한 방향으로 이동
                # 3) 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_horse_index_array = []

            # 말위에 말들이 있다면 한번에 이동해야 됨
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                # 여기서 이동해야 하는 애들은 현재 옮기는 말 위의!!! 말들이다.

                # 현재말의 인덱스를 찾음
                if horse_index == current_stacked_horse_index:
                    # 현재 말부터 나머지까지 moving_horse_index_array에 저장
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    # 기존 말들은 그대로 냅두기
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            # 2) 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            #
            for moving_horse_index in moving_horse_index_array:
                # 이동한 말들을 current_stacked_horse_map에 업데이트
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)

                # horse_location_and_directions 에 이동한 말들의 위치를 업데이트한다.
                # 말들의 위치 값들을 변경 , 방향은 그대로
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][
                    1] = new_r, new_c

            # 해당 위치에 말들이 총 4개있다면 한칸에 4개의 말이 있다고 간주 게임 종료
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                # 총 실행된 횟수를 리턴
                return turn_count

        # 매턴마다 +1 씩 턴 값 증가
        turn_count += 1

    #  1000회까지도 성공하지 못했다면 -1 리턴
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
