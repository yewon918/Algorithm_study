from collections import defaultdict, deque

def solution(arrows):
    answer = 0

    visit = defaultdict(int)        # 방문확인
    visit_loc = defaultdict(int)    # 노드 확인
    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

    loc = (0,0)
    deq = deque([loc])      # 현 위치

    for direc in arrows:
        for _ in range(2):
            next = (loc[0]+directions[direc][0], loc[1]+directions[direc][1])
            deq.append(next)
            loc = next

    now = deq.popleft()
    room = 0
    visit[now] = 1

    while deq:
        next = deq.popleft()
        if visit[next] == 1:
            if visit_loc[(next, now)] == 0:
                room += 1
        else:
            visit[next] = 1
        visit_loc[(now, next)] = 1
        visit_loc[(next,now)] = 1
        now = next

    answer = room

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
