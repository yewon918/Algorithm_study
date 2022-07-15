def solution(rows, columns, queries):
    answer = []
    # 1:00

    graph = [list(range(1+(i*columns), 1+(i*columns)+columns)) for i in range(rows)]
    # list니까 []로 하는게 맞음. 괄호 생각 잘하자

    for query in queries:
        x1, y1, x2, y2 = query
        temp1 = graph[x1-1][y2-1]
        temp2 = graph[x2-1][y2-1]
        temp3 = graph[x2-1][y1-1]
        ans = min(temp1, temp2, temp3)

        for i in range(x1-1, x2-1):
            graph[i+1][y2-1] = graph[i][y2-1]
            ans = min(graph[i+1][y2-1], ans)
        for i in range(y2-1, y1-1, -1):
            graph[x2-1][i-1] = graph[x2-1][i]
            ans = min(graph[x2-1][i-1], ans)

        for i in range(x2-1, x1-1, -1):
            graph[i][y2-1] = graph[i-1][y2-1]
            ans = min(graph[i][y2-1], ans)
        for i in range(y2-1, y1-1, -1):
            graph[x1 - 1][i] = graph[x1 - 1][i - 1]
            ans = min(graph[x1 - 1][i], ans)

        graph[x1][y2-1]=temp1
        graph[x2-1][y2-2]=temp2
        graph[x2-2][y1-1]=temp3
        answer.append(ans)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))