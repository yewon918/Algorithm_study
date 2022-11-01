'''
연속된 N일동안 매매가 예측
하루 최대 1 구입, 판매 제한 없음

구입: 3
판매 6-3/ 판매가 * 개수 - 구입 가격 누적해서 더하기
최대 이익 출력

첫줄 - 테스트케이스 수
----
판매해서 최대인 경우:
'''

case = int(input())

for tc in range(case):
    N = int(input())    # 날 수
    arr = list(map(int, input().split()))

    max = arr[-1]   # 제일 끝값이 max값이라 설정
    profit = 0
    for now in range(N-2, -1, -1):
        if arr[now] >= max:
            max = arr[now]    # 최대값 변경
        else:
            profit += max - arr[now]
    print('#{} {}'.format(tc+1, profit))
