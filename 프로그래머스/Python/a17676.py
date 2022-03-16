from datetime import datetime, timedelta


def solution(lines):
    answer = 0

    lines_list = [list(line.split()) for line in lines]
    start_end_times = []
    check_times = []

    for D, S, T in lines_list:
        mili_sec = int(round(float(T[:-1]), 3) * 1000 - 1)
        end = datetime.strptime(D + ' ' + S, "%Y-%m-%d %H:%M:%S.%f")
        start = end - timedelta(milliseconds=mili_sec)  # ....?

        start_end_times.append((start, end))
        check_times.append(start)
        check_times.append(end)

    cnt_list = []
    for i in range(len(check_times)):
        traffic_start = check_times[i]
        traffic_end = traffic_start + timedelta(milliseconds=999)
        cnt = 0
        for start, end in start_end_times:
            # 끝점이 트래픽 시간에 포함
            if start <= traffic_start and end >= traffic_start:
                cnt += 1
            # 시작점이 트래픽 시간에 포함
            elif start <= traffic_end and end >= traffic_end:
                cnt += 1
            # 모든부분이 트래픽 시간에 포함
            elif start >= traffic_start and end <= traffic_end:
                cnt += 1
        cnt_list.append(cnt)

    answer = max(cnt_list)

    return answer

lines = ["2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"]
print(solution(lines))