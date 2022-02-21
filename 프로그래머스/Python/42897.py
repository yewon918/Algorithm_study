'''
인접한 집들과 방범장치 연결됨
인접한 두 집 - 경보 울림

경보를 울리지 않고 도둑이 최대한으로 돈을 훔쳐야함
* 턴 집의 양 옆을 털면 안됨
enumerate해서 최댓값 순으로 sort, 각 인덱스가 양 옆에 위치하는지 판단
최대로 털수 있는 집의 개수 - 5//2 이런식인가 그럼
최대 개수에 이르는지 확인 + 바로 옆인지도 확인
금액에 집중
'''
def solution(money):

    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    dp1[0] = money[0]
    for i in range(1, len(money)-1):    # 0을 포함
        dp1[i] = max(dp1[i-2]+money[i], dp1[i-1])

    dp2[0] = 0
    for j in range(1, len(money)):
        dp2[j] = max(dp2[j-2]+money[j], dp2[j-1])

    return max(dp1[-2], dp2[-1])

print(solution([1,2,3,1]))