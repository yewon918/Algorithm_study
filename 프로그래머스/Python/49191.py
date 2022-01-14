'''
9:20까지
정확하게 순위를 매기는 선수의 수 return
알게 되면 배열 하나에 다 넣어주기
3명에게 패배, 1명 승리 -> 4위
맨 앞 원소로 그래프 형성, 각 그래프에 연결된 노드가 나올때마다 visited에 값 올려주기,
visited 값 만큼 패배했다는 뜻 - 순위 알 수 있음
순위 확인 하는 소스
순ㅇ위가 분명할 경우, 그 수에 진 수의 순위 확인 가능
'''
from collections import deque
def solution(n, results):
    answer = 0
    graph=[[] for _ in range(n+1)]
    deq = deque([1])
    visited = [[0,0] for _ in range(n+1)]     # 승리, 패배 횟수를 센다
    sure = []

    for win, lose in results:
        graph[win].append(lose)

    while deq:
        node = deq.popleft()
        for check_lose in graph[node]:
            visited[check_lose][1] += 1        # visited[0]은 고려되지 않고 각 인덱스 별로 센다
            sum = visited[check_lose][1] + visited[check_lose][0]
            if sum is not None and sum == len(n):       # 등수가 확실
                sure.append(check_lose)
            deq.append(check_lose)
            if visited[check_lose] in sure:
                for i in deq:
                    if i in visited[check_lose]:
                        sure.append(check_lose)

    answer = len(sure)

    return answer

print(solution(n=5, results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))