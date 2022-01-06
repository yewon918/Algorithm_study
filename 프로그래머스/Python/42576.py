'''
단 한명 제외, 모두 마라톤 완주
마라톤 참여자 이름: participant
완주한 선수: completion
완주하지 못한 선수 이름 return
- 참가자 중 동명이인 있음

'''

# def solution(participant, completion):
    # answer = ''
    #
    # for k in participant:
    #     if k not in completion:
    #         answer = k
    #         break
    #     else:
    #         for j in range(len(completion)):
    #             if k == completion[j]:
    #                 completion[j] = ''
    #                 break
    # return answer
# remove를 쓸 수도 있네 그러고보니까

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort() # sort 하면 비교문에서 빠름
    for i in range(len(participant)-1):
        if(participant[i]!=completion[i]):
            return participant[i]
    answer = participant[-1]
    return answer

participant = ["mislav", "stanko", "z", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))
