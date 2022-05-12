'''
NxM - 공격 -> 0이하면 파괴
아군) 스킬 회복
이미 파괴된 건물도 내구도 하락 가능
1 - 적의 공격
2 - 히복스킬
# 파괴 되지 않은 건물 수 리턴
----
맵 만들기
for문에 넣어주기

'''
def solution(board, skill):
    answer = 0
    imos_map = ([0]*(len(board)+1) for _ in range(len(board)+1)





    return answer


print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
# [type, r1, c1, r2, c2, degree]
# [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
