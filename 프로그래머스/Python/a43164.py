def solution(tickets):
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]]=[ticket[1]]

    for k in t.keys():
        t[k].sort(reverse=True)     # 도착지를 역순으로 넣는다

    st=["ICN"]
    answer = []

    while st:
        top = st[-1]
        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())
    answer.reverse()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
