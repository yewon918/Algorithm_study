'''
두 팀으로 나눠서 진행, 상대 팀 진영 먼저 파괴 -> 최대한 빨리 도착
게임 캐릭터, 첫 위치
주위에 벽이 있으면 도착하지 못할 수도 있음 return -1
지나가야 하는 칸의 개수 최소값 return
길 1, 벽 0
-----
maps[i][j]

최단거리 - bfs
큐 - 만나는 길에 1이 있을 경우 해당 좌표 저장
방향 4개 저장, 현재 좌표에 더해봐야할거 같음 -> 1이 있는지 검색


'''
from collections import deque
def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = [[False]*M for j in range(N)]

    que = deque()
    # row+1, col+1, row-1, col-1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    que.append((0, 0))      # 현재 위치
    visited[0][0] = True

    if maps[N-2][M-1] == 0 and maps[N-1][M-2] == 0:
        return -1

    while que:
        cx, cy = que.popleft()
        for k in range(4):
            x = cx + dx[k]
            y = cy + dy[k]

            if 0 <= x < N and 0 <= y < M:
                if maps[x][y] == 1 and visited[x][y] == False:
                    maps[x][y] = maps[cx][cy] + 1
                    que.append((x, y))
                    visited[x][y] = True

            if not (0 <= x < N and 0 <= y < M):
                continue
            if maps[x][y] == 0:
                continue
            if maps[x][y] == 1:
                maps[x][y] = maps[cx][cy]+1
                que.append((x, y))
                visited[x][y] = True


    answer = maps[N-1][M-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
