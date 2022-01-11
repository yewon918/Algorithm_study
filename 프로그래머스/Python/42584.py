'''
주식가격이 담긴 배열 prices
return - 가격이 떨어지지 않은 기간 초들 반환

deq 자료형 popleft - deq에서 다음 수들 확인
deq 안에 자기보다 작은 수 있으면, 정지하고, 해당 인덱스+1까지의 값 출력
enumerate를 사용,
해당 인덱스 - 자기 값
'''
from collections import deque
def solution(prices):
    answer = []
    
    deq = deque([(i, v) for i, v in enumerate(prices)])
    # i가 인덱스 번호
    while deq:
        num = deq.popleft()

        for l in deq:
            if num[1] > l[1]:
                break
        time = l[0] - num[0]
        answer.append(time)


    return answer

prices = [1,2,3,2,3]
print(solution(prices))
