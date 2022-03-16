'''
초당 최대 처리량 계산
응답완료시간 S, 처리시간 T 가 공백
2016-09-15 hh:mm:ss.sss
lines 배열 - S : 고정길이, T : 최대 소수 3자리까지 s
응답완료시간 S를 기준으로 오름차순 정렬
return - 초당 최대 처리량
-----
1초를 어디서부터 어디까지 잡을 것인가
각 정렬된 것들의 시작점+1초가 얼마나 포함하는지 봐야겠다
시작점 구하는 법: ss.sss - T
시작점을 구하고 -> 각 시작점 +1의 범위에 들어오는지 판단
---
2016-09-15 hh:mm:ss.sss
11:59:59.01 ~ 12:00:00.01 은 어떻게 하지? 어차피 추석 하루만 처리.

3씩 범위를 뛰었을때
그 다음 초의 숫자가 작다면, +59:+60 해서 생각해주자
'''
def solution(lines):
    answer = 0
    start = []

    time = []
    for line in lines:
        for i in range(3):
            time.append(line.split()[1].split(':')[i])
        time.append(line.split()[2].split('s')[0])
        print(time)
    for sec in range(0, len(time), 4):
        second = float(time[2+sec])
        tsecond = float(time[3+sec])
        if tsecond > second:
            second += 60
            time[1+sec] -= 1
        tmp = second - tsecond

        start.append(float(''.join([time[sec], time[1+sec], str(tmp)])))

    for point in range(len(start)):
        a = 0
        for check in start[point:]:
            if start[point] <= check <= start[point]+1:
                a+=1
        if answer < a:
            answer = a

    return answer

lines = ["2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"]
print(solution(lines))
