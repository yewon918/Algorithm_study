'''
중요도가 높은 문서 먼저 인쇄
1. 가장 맨앞 문서를 대기목록에서 꺼내기
2. 나머지에서 j보다 중요도가 높은게 하나라도 있으면 j를 대기목록 가장 마지막에
3. or j 인쇄

숫자가 클수록 중요도 높음
중요도가 순서대로 담긴 배열 priorities, 내가 요청한 문서 현재 위치 location
location이 몇번째로 인쇄되는지 return

1<=  <=100
중요도는 1~9
location의 인덱스는 0부터 시작

재배치 후 index를 세나? - 같은 수가 여러개, 해당수를 --1 이런식으로 변경?

pop하면서 push하지 않을때 +1 을 해야함
동시에 priorities[location]의 순서 조절
앞이 빠질 경우 -1, 뒤로 갈 경우 +배열 크기 만큼

answer는 location
'''
from collections import deque
def solution(priorities, location):
    answer = 0

    # tmp = priorities[location]
    deq = deque(priorities)
    while deq:
        first = deq.popleft()
        location -= 1       # 맨 앞을 뽑아내면 location의 크기가 즐어듦
        for i in deq :   # 남은 원소들 중 비교
            if i > first:
                deq.append(first)
                # location에 해당하는게 뒤로 간다면, location크기 늘어남
                if location == -1:
                    location = len(deq)-1   # location의 크기 +1
                break
        if first == max(priorities):
            break
        if location == -1:   # location이 맨앞이라면 while문 종료
            break

        # 다 돌았는데 없으면 pop
    answer = location + 2

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))