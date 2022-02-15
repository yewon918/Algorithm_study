def solution(tickets):
    answer = []
    dest = dict()

    for ticket in tickets:
        if ticket[0] in dest:
            dest[ticket[0]].append(ticket[1])
        else:
            dest[ticket[0]] = [ticket[1]]       # []

    for i in dest:
        dest[i].sort(reverse=True)      # 리스트 역순

    stack = ['ICN']

    while stack:
        top = stack[-1]
        if top not in dest or len(dest[top]) == 0:
            answer.append(top)
            stack.pop()
        else:                   # 도착지가 있는 애였을 때
            stack.append(dest[top][-1])     # 리스트 맨 뒤
            dest[top].pop()

    answer.reverse()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
