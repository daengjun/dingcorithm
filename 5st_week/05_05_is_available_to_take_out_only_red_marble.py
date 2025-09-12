from collections import deque

# 문제 설명
# 보드 내에 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
# '.'은 빈 칸을 의미하고,
# '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
# 'O'는 구멍의 위치를 의미한다.
# 'R'은 빨간 구슬의 위치,
# 'B'는 파란 구슬의 위치이다.

# 위에서 패턴이 아무것도 안보임 -> 모든 경우의 수 확인 -> BFS
# Queue -> visited [0,1,3,4]
# 2배열을 기준으로 방문했는지 여부를 확인

#  파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼수 있으면  True , 없으면 False를 반환한다.
#  -> 모든 수를 탐색해도 괜찮은 범위다.

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

#     북  동  남 서
dr = [-1, 0, 1, 0]  # row - 가로
dc = [0, 1, 0, -1]  # colum - 세로


# 벽이거나 구멍이 아닐때 까지 구슬을 굴리는 함수
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    # n은 전체 인덱스 , game_map[0]은 배열 하나에 들어있는 인덱스
    n, m = len(game_map), len(game_map[0])

    # 4차원 배열 생성
    # [빨강구슬(red_row)][빨강구슬(red_col)][파랑구슬(blue_row)][파랑구슬(blue_col)]
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # FIFO
        if try_count > 10:  # 10 이하여야 한다.
            break

        for i in range(4):
            # 벽이나, 구멍이 아닐때까지 이동
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            # 성공 여부 확인
            # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
            if game_map[next_blue_row][next_blue_col] == 'O':
                continue

            # 빨간 구슬이 구멍에 떨어진다면(성공)
            if game_map[next_red_row][next_red_col] == 'O':
                return True

            # 같은 위치라면 더많이 이동한 구슬을 한칸뒤로 이동
            if next_red_row == next_blue_row and next_red_col == next_blue_col:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True

                # 이동한 위치 queue에 저장
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))
