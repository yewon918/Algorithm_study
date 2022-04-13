# 8:40-9:10
'''
1번 음식부터 회전판 번호 증가 순서대로 가져옴
1초 섭취 후 다음음식
K초 후 네트워크 장애
K초 후 뭘 먹어야하는지 리턴
----
%로 배열을 반복문으로 돌리면서 시행
0이면 skip
k초에 뭘 먹어야하는지 보기
'''
def solution(food_times, k):
    answer = 0
    fsize = len(food_times)

    cnt =0
    pnt = 0
    next = 0
    for i in range(0, k):     # k까지 돌리고
        pnt = i % fsize
        next = (i + 1) % fsize

        # 음식 시간을 -1 씩 줄임
        if food_times[pnt] == 0:
            pnt += 1
        food_times[pnt] -= 1

    # 다음 음식 찾기
    if food_times[next] != 0:   # 다음 음식이 0이 아닌 경우
        answer = next+1
    else:                       # 다음 음식이 0이라 찾아야할 경우
        for j in range(fsize):     # 0이 아닌거 찾기
            if cnt == fsize: return -1
            if food_times[(pnt+j) % fsize] == 0:
                cnt += 1
                continue
            else:
                answer = (pnt+j) % fsize +1
                return answer

    return answer

print(solution([1,1,1], 2))