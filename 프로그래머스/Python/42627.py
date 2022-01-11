'''
4:10까지 문제 풀이
4:30까지 답 보기
4:50까지 다시 풀기

한 번에 하나의 작업만 수행
요청이 들어온 순서대로 처리 -> 우선순위 큐 --> 힙
2차원 배열 jobs [작업이 요청되는 시점, 작업의 소요시간]
작업 요청부터 종료까지 걸린 시간 평균 가장 줄이는 방법으로, 이때의 평균 return
- 작업수행 안할 경우 먼저 들어온 순서부터
----
평균을 가장 줄이는 방법 -
걸린시간 = 완료 - 요청시간
우선순위를 뭘로 둬야하지? --> 처리하는데 걸리는 시간

시작 - 제일 먼저 들어온 작업부터
min heap - 내부적으로 최소힙 형태로 저장

answer = jobs[0][1]
시간 계산 필요 - 작업시간들 전부 더하고, 작업이 끝날때마다 해당 요청 시간을 빼주기 => 저장 store / len(jobs)
    # 2번째 원소 기준으로 minheap 구현
    # 2번쨰 원소가 작은걸 pop하고, 할 때마다 두번쨰 원소 값 더하기 && 요청 시간 빼기
    # value - 두번째 원소 값을 더함.
    # work - value - 첫번째 시간
    # avg - work 저장

'''

import heapq
import sys


def solution(jobs):
    answer = 0
    i = 0
    start = -1
    now = 0
    heap = []
    while i < len(jobs):
        for j in jobs:      # 도착, 소요
            if start < j[0] <= now:
                heapq.heappush(heap,(j[1], j[0]))
        if len(heap)>0:
            curr = heapq.heappop(heap)  # 소요, 도착
            start = now
            now += curr[0]
            answer += now - curr[1]     # 걸린시간 - 처음 도착시간
            i += 1
        else:
            now += 1

    return answer//len(jobs)


print(solution(jobs=[[0, 3], [1, 9], [2, 6]]))