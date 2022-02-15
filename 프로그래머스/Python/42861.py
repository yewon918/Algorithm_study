# kruskal 알고리즘 - MST 사용, 최소의 비용으로 사이클을 형성하지 않음

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # kruskal1 - 오름차순 정렬
    # costs 내부 원소들을 기준으로 sorting 할건데 그 내부의 2번째 원소 기준으로

    candi = set([costs[0][0]])      # 주의!

    while len(candi) != n:          # kruskal2 - 사이클 형성하지 않으면서 연결
        for i in costs:
            if i[0] in candi and i[1] in candi:
                continue
            if i[0] in candi or i[1] in candi:
                candi.update([i[0], i[1]])      # 주의!!
                answer += i[2]
                break       # candi 수 안넘는거 확인해야함

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))