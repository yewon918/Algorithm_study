from collections import deque
def solution(people, limit):
    deq = deque(sorted(people, reverse=True))
    answer = 0

    comp = len(deq) - 1
    while comp >= 0:
        if len(deq) == 1:
            deq.popleft()       # 인덱스 0 지움
            answer += 1
            break
        if deq[0]+deq[comp] > limit:
            if comp != len(deq) - 1:
                deq.remove(comp+1)

        else:       # 합이 limit와 크거나 같을 때
            deq.pop()
            comp -= 1

        deq.popleft()
        answer+= 1
        comp -= 1

    return answer

print(solution([70, 50, 80, 50], 100))