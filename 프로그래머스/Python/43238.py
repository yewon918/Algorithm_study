"""
한 심사대에 한명만 ㄱㄴ
걸리는 시간을 최소로
입국 심사 기다리는 사람 수 n, 심사관이 한 명 심사에 걸리는 심사관 당 시간 times
return:심사받는데 걸리는 최소 시간
7 10
1 2
3 4
5
6

시간이 걸리는 경우의 수를 모두 계산

"""
def solution(n, times):
    answer = 0
    right = max(times)*n
    left = 0

    while left<=right:
        mid = (left+right)//2
        people = 0

        for i in times:
            people += mid // i   # 각 심사관에게 주어진 시간
            if people >= n:
                answer = mid
                right = mid -1
                break
        if people<n:
            left = mid + 1
    return answer

print(solution(n=6, times=[7,10]))