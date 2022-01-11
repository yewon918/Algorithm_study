 # 1 ~ n 까지 번호 -> 1번 노드에서 제일 멀리 떨어진 노드 '개수'(간선의 개수)
 # 노드 개수 n, 간선 정보 2차원 배열 vertex : edge
 # 간선을 몇개 지났는지 세고 간선의 개수가 max인 것들()을 넣으면 되겠다
 # 간선 개수 세기 - 이차원 배열 형성, 3번 인덱스에 각 원소들 추가
 # 1 - 3, 2
 # 2 - 3, 1, 4, 5
 # 3 - 6, 4, 2, 1
 # 4 - 3, 2
 # 5 - 2
 # 6 - 3

from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [-1]*(n+1)   # 방문 확인

    # edge에서 a, b를 뽑아내서 그래프 생성
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 방문 예정 노드 설정, 방문 처리
    deq = deque([1])
    visited[1] = 0

    # deq에 있는 노드들을 하나씩 반복한다
    while deq:
        node = deq.popleft()  #deq에 있는 node를 방문해볼 예정
        for next_node in graph[node]:
            if visited[next_node] == -1:      # 아직 방문하지 않음
                deq.append(next_node)       # 다음 방문예정 큐에 넣음
                visited[next_node] = visited[node] + 1  # 거리를 설정, 현재node+1

    # node
    max_d = max(visited)
    for i in visited:
        if i == max_d:
            answer += 1

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))