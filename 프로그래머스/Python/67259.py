'''
1 - 벽(가능), 0 - 비었음(불가능)
좌측 상단 -> 우측 하단 (0,0) -> (n-1, n-1)
직선도로 : 100원 - 한칸 지날때 마다 100
코너 : 500원
3~25

+1 되는 col, row가 같으면 직선도로/ 더해지는게 바뀌면 코너
경로 여러개 가능, 더 적은 비용 경로 선택
-----
완전탐색? - 가능한 모든 경우의 수를 전부 체크 -> bfs 활용
    경우의 수 -> 25*25
최단거리, 임의의 경로 문제 bfs - 최단거리가 최단거리가 아닐수도..
-----
그래프를 생성해야할까?
상하좌우가 0이라면 움직임
(n-1,n-1) 위치라면 정지, 비용리스트에 넣기
'''
from collections import deque
def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N = len(board[0])

    answer = float('inf')
    deq = deque([])
    cost = [[[float('inf') for y in range(len(board))] for x in range(len(board))] for z in range(4)]

    for z in range(4):      # 방향을 추가해줌
        cost[z][0][0] = 0

    if board[1][0] != 1:    # x
        deq.append([1, 0, 100, 1])
        cost[1][1][0] = 100

    if board[0][1] != 1:    # y
        deq.append([0, 1, 100, 3])
        cost[3][0][1] = 100

    while deq:
        x, y, price, dir = deq.popleft()    # popleft다, 주의하자

        for i in range(4):      # 방향 비교, 범위 0~3
            nx = x+dx[i]
            ny = y+dy[i]
            tmp_price = price + 100 if i == dir else price + 600

            if 0 <= nx < N and 0 <= ny < N:
                if tmp_price < cost[i][nx][ny] and board[nx][ny] == 0:
                    deq.append([nx, ny, tmp_price, i])
                    cost[i][nx][ny] = tmp_price

    for z in range(4):
        if answer > cost[z][N-1][N-1]:
            answer = cost[z][N-1][N-1]


    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))