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

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(board):
    answer = 0
    N = len(board)
    start, end = (0, 0), (N - 1, N - 1)
    costs = [[float('inf')] * N for _ in range(N)]
    # inf - 양의 무한대

    deq = deque()
    deq.append((0, 0, 0, 1))    # 좌
    deq.append((0, 0, 0, 3))    # 상
    costs[0][0] = 0     # 현재 비용: 0원
    while deq:
        x, y, cost, dir = deq.popleft()     # 좌표, 비용, 방향
        for k in range(4):      # 상하좌우 하나씩 좌표를 움직임
            nx = x + dx[k]
            ny = y + dy[k]
            tmp_cost = cost + 100 if dir == k else cost + 600   # 좌||상이면 100
            if 0 <= nx < N and 0 <= ny < N:     # 범위 체크
                if board[nx][ny] == 0 and tmp_cost <= costs[nx][ny]:    # 벽이 아닌지, 최소 값이 맞는지
                    costs[nx][ny] = tmp_cost        # 비용 설정
                    deq.append((nx, ny, tmp_cost, k))   # append

    answer = costs[end[0]][end[1]]

    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))