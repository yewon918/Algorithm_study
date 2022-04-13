'''
NxM - 공격 -> 0이하면 파괴
아군) 스킬 회복
이미 파괴된 건물도 내구도 하락 가능
1 - 적의 공격
2 - 히복스킬
# 파괴 되지 않은 건물 수 리턴
----
맵 만들기
for문에 넣어주기

'''
def solution(board, skill):
    answer = 0
    # 시작점, 끝점, 가중치를 입력해둘 배열
    imos = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for row in skill:
        # 명령 쿼리에 따라 imos 배열에 4개의 꼭짓점에 각각 해당하는 값을 지정한다.
        if row[0] == 1:
            imos[row[1]][row[2]] += -row[5]
            imos[row[3] + 1][row[2]] += row[5]
            imos[row[1]][row[4] + 1] += row[5]
            imos[row[3] + 1][row[4] + 1] += -row[5]
        else:
            imos[row[1]][row[2]] += row[5]
            imos[row[3] + 1][row[2]] += -row[5]
            imos[row[1]][row[4] + 1] += -row[5]
            imos[row[3] + 1][row[4] + 1] += row[5]

    # imos 배열을 가로, 세로로 훑으면서 입력해둔 값을 통해 진짜 값을 계산
    # 가로
    for i in range(len(imos)):
        now = 0
        for j in range(len(imos[0])):
            now += imos[i][j]
            imos[i][j] = now
    # 세로
    for i in range(len(imos[0])):
        now = 0
        for j in range(len(imos)):
            now += imos[j][i]
            imos[j][i] = now

    # 마지막으로 board 배열과 합치면서 0보다 큰 값의 개수를 구한다.
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
# [type, r1, c1, r2, c2, degree]
# [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
