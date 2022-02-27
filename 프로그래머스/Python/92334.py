'''
여러번 신고 가능, 동일 유저 신고 횟수는 1회로 처리
k번 이상 신고시, 게시판 이용 정지, 신고한 모든 유저에게 정지 사실 알림
마지막에 한꺼번에 게시판 이용 정지 시킴

id_list
report - 이용자 +신고당한 애
정지 기준 k

return - id_list 순서대로 유저가 받은 결과 수 담기
------
사전자료형 value에 넣기


'''
def solution(id_list, report, k):
    answer = []
    warn = {}
    monitor = []

    # key 만들어주기
    for list in id_list:
        warn[list] = [0, [], 0]

    # key에 value 넣어주고 걸릴때마다 +1 해주기
    for name in report:
        reporter, reported = name.split()
        if reported not in warn[reporter][1]:    # 이미 신고 당한 적 없으면 신고횟수 올려주기
            warn[reported][0] += 1
        warn[reporter][1].append(reported)

    for find in warn:
        if warn[find][0] >= k:     # 신고 당한 횟수가 k보다 크거나 같다면
            for check in warn:
                if find == warn[check]: break
                else:
                    if find in warn.get(check)[1]:    # 신고한 이력이 있음
                        warn[check][2] += 1

    for i in warn:
        answer.append(warn[i][2])

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))