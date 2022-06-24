from collections import deque

def solution(N, road, K):
    answer = 0

    node = {}
    for v1, v2, distance in road:
        node[v1] = node.get(v1, []) + [(v2, distance)]
        node[v2] = node.get(v2, []) + [(v1, distance)]

    dist = {i:float('inf') if i != 1 else 0 for i in range(1, N+1)}

    deq = deque([1])
    while deq:
        current = deq.popleft()
        for next, dis in node[current]:
            if dist[next] > dist[current] + dis:
                dist[next] = dist[current]+dis
                deq.append(next)

    answer = len([True for i in dist.values() if i <= K])
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))