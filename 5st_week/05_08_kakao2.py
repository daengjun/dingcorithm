import math

# C#처럼 #붙은 애들을 소문자로 치환
def replace_step(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = None
    # 가장긴 시간 반환
    max_play_time = 0
    m = replace_step(m)

    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(",")
        play_time = (int(end_time[:2]) * 60 + int(end_time[3:])) - (int(start_time[:2]) * 60 + int(start_time[3:]))

        melody = replace_step(melody)
        # math.ceil ← 올림
        # math.round ← 반올림
        melody_repeated_count = math.ceil(play_time / len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]
        if m in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time

    # 일치 하는게 없다면
    if not answer:
        return "(None)"

    return answer
