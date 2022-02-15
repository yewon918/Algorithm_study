from collections import deque
def solution(tickets):
    answer = []
    stack = deque([])
    visited = [False for i in range(len(tickets))]

    stack.append(tickets[0][0])   # icn으로 시작합니다

    while stack:
        top = stack.pop()
        answer.append(top)
        for ticket in range(len(tickets)):
            if visited[ticket] == True or tickets[ticket][0] != top:
                continue                        # true면 그냥 넘어간다
            else:                               # 같다면
                if len(stack):                  # stack이 비지 않았다면 하나 pop해서 확인
                    tmp = stack.pop()
                    if tickets[ticket][1] > tmp:    # pop한 게 더 앞에 오는 문자라면, 원상복구
                        put = tmp
                    else:
                        put = tickets[ticket][1]
                        idx = tickets.index([tickets[ticket][0], tmp])
                        # print(idx)
                        visited[idx] = False
                        visited[ticket] = True
                    stack.append(put)
                else:
                    visited[ticket] = True
                    stack.append(tickets[ticket][1])

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))