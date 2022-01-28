# floyd-warshall: dp
# def solution(n, results):
#     answer = 0
#     beat = [[None for _ in range(n+1)] for _ in range(n+1)]  # 승패 확인이 되지 않은 상태
#
#     for win, lose in results:       # 승패를 입력함
#         beat[win][lose] = True
#         beat[lose][win] = False
#
#     #floyd-warshall 식 접근
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             for k in range(1, n+1):
#                 if beat[i][j] == None:      # 승패가 확인되지 않았다면 넘김
#                     continue
#                 if beat[j][i] == beat[i][k]:
#                     beat[j][k] = beat[i][k]
#                     beat[k][j] = not beat[i][k]
#
#     for l in range(1, n+1):
#         if None in beat[l][1:l] + beat[l][l+1:]:       # 자기 자신을 제외하고 고려해봄
#             continue
#         answer += 1
#
#     return answer


from collections import defaultdict
def solution(n:int,results:list)->int:
    answer = 0
    winners, losers = defaultdict(set), defaultdict(set)    # 중복을 제거하는 딕셔너리 자료형

    for win, lose in results:       # 이긴사람과 진 사람 항목 따로 만들기
        winners[win].add(lose)
        losers[lose].add(win)

    for i in range(1, n+1):
        for winner in losers[i]:
            winners[winner].update(winners[i])      # ...?
        for loser in winners[i]:
            losers[loser].update(losers[i])

    for j in range(1, n+1):
        if len(winners[j]|losers[j]) == n-1:
            answer +=1

    return answer

print(solution(n=5, results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))