# https://www.daleseo.com/python-enumerate/
from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque([(i, v) for v, i in enumerate(priorities)])
    # 원래는 순서가 앞, value가 뒤에 오지만, v,i를 바꿈
    while deq:
        first = deq.popleft()
        if deq and max(deq)[0] > first[0]:
            deq.append(first)
        else:
            answer += 1
            if first[1] == location:
                break

    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities,location))