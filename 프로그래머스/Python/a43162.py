def dfs(x, computers):
    computers[x][x]=2
    for j in range(len(computers[x])):
        if computers[x][j] == 1 and computers[j][j] != 2:
            dfs(j, computers)


def solution(n, computers):
    answer = 0
    for i in range(len(computers)):
        if computers[i][i] == 1:
            dfs(i, computers)
            answer += 1

    return answer

print(solution(3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))