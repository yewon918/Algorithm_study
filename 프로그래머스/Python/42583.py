"""
모든 트럭이 다리를 건너려면 걸리는 시간
bridge_length

2대 올라감, 10kg 까지 견딤
2대 올라가면 초가 1초씩, 한대만 올라가면 초 2초씩
- 하나 당 2초씩

deq에 넣음 - 큐
input 할때 +1초
while:
    합이 <10일 경우 deq에 있을 수 있음
    (input마다 +1)
if 하나이고, 다른 트럭이 올라올 수 없었을때 :
    시간 +1
"""
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    truck_weights = deque(truck_weights)

    while bridge:
        bridge.pop(0)
        answer += 1
        if sum(truck_weights) > 0 :
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return answer

print(solution(bridge_length=2, weight=10, truck_weights=[7,4,5,6]))