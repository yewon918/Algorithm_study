# floyd-warshall: dp
# def solution(n, results):
#     matrix = [[None for _ in range(n)] for _ in range(n)]
#     for win, lose in results:
#         matrix[win - 1][lose - 1] = True
#         matrix[lose - 1][win - 1] = False
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if matrix[j][i] == None:
#                     continue
#
#                 if matrix[j][i] == matrix[i][k]:        # ex, j가 i에게 짐, i가 k에게 짐
#                     matrix[j][k] = matrix[i][k]
#                     matrix[k][j] = not matrix[i][k]
#
#     answer = 0
#     for i in range(n):
#         if None in matrix[i][:i] + matrix[i][i+1: ]:   # 전체를 봄  - none이 있다면 승패를 알 수 없음
#             continue
#         answer += 1
#     return answer


from collections import defaultdict
def solution(n:int,results:list)->int:
    # 정확하게 순위를 매길 수 있는 선수들의 수를 구한다.
    # 한 선수가 다른 선수와 경쟁했을 때, 이기고 진 횟수의 합이 정확하게 n-1번 이라면 이 선수의 순위를 알 수 있다
    # 먼저 results의 결과를 통해 결과를 만든다.
    # 그 후 results의 결과를 통해 유추할 수 있는 결과를 갱신한다
    answer=0
    win,lose = defaultdict(set),defaultdict(set)
    # defaultdict - 딕셔너리를 만드는 dict 클래스의 서브클래스
    # : 처음 키를 지정할때 값을 주지 않으면 키에 대한 값을 디폴트 값으로 설정

    for result in results:
        win[result[0]].add(result[1])       # 0이 1에게 이김
        lose[result[1]].add(result[0])      # 1이 0에게 짐
    for i in range(1,n+1):
        for winner in lose[i]: win[winner].update(win[i]) # 힘의 우열로 인해 a가 이긴 사람 다이김
        for loser in win[i]: lose[loser].update(lose[i]) # 힘의 우열로 인해 a가 진 사람께 다 짐
    for i in range(1,n+1):
        if len(win[i]|lose[i]) == n - 1:
            answer += 1
    return answer

print(solution(n=5, results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))