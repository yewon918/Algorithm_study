"""
m, n이 1인 경우는 입력으로 주어지지 않음
- 집과 학교는 물에 잠기지 않음
- 물에 잠긴 지역 0 ~ 10개
y가 내려갈수록 +, x가 오른쪽일수록 +
puddles를 피해서 최단경로의 개수
%1,000,000,007
-----
[[2,2]]
dy, dx
    상하좌우 -> 하,우만 사용
dy=[-1, 1, 0, 0]
dx=[0, 0, 1, -1]
[4,3]
1, 1을 빼고 더한 값이 지나간 길 수
"""
def solution(m, n, puddles):
    # m-우, n-하
    answer = 0
    dp = [[0]*(m+1) for i in range(n+1)]

    dp[1][1] = 1    # 집
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue
            if [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    answer = dp[n][m] % 1000000007
    return answer

print(solution(m=4, n=3, puddles=[[2,2]]))