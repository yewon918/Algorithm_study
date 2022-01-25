"""
각 배열에 연결정보 표시
visited
"""

def solution(n, computers):
    answer = 0
    cnt = 0
    visited = [0 for i in range(n)]

    for i in computers:
        print("i체크", i)
        cnt = 0
        for j in i:
            if j == 1:
                visited[cnt] += 1
                print("visited임", visited)
            cnt += 1

    check = max(visited)

    for i in visited:
        if i == check:
            answer += 1

    return answer

print(solution(3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))