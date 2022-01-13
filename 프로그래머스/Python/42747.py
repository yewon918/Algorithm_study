'''
n편 중 h번 이상 인용된 논문
인용횟수 citations
h-index n편 중 h번 이상 인용된 논문이 h번 이상, 나머지가 h번 이하 인용
----
3,0,6,1,5 --> 3

'''
# [2,18,22,23]
def solution(citations):
    citations.sort(reverse=True)
    h=len(citations)

    while True:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1    # cnt는 인용수
            if cnt >= h:
                return h
        h -= 1
    return answer

print(solution(citations=[3, 0, 6, 1, 5]))