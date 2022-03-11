'''
k개의 방 , 1~k번까지 번호로 구분
신청한 순서대로 방 배정, 비어있다면 바로 배정,
이미 배정 - 원하는 방보다 번호가 크면서 비어있는 방 중 가장 작은 방
------
방번호 - 인덱스로 생각
true/false로 표시
for문을 통해 false인거 찾기
인덱스를 넣어주기
'''
def solution(k, room_number):
    answer = []
    room = {}

    for num in room_number:
        recom = room.get(num, 0)   # room[num]의 value (그다음 방) || 0
        if recom:      # 그 다음 방을 추천한다면?
            tmp = [num]
            while True:
                idx = recom
                recom = room.get(recom, 0)      # 갱신
                if not recom:    # 추천한 방이 비었다면
                    room[idx]= idx+1    # 으ㅏㅇ어ㅏ앙아아ㅏㅇ나아
                    answer.append(idx)
                    for i in tmp:
                        room[i] = idx + 1
                    break
                tmp.append(recom)
        else:
            room[num] = num+1
            answer.append(num)

    return answer

print(solution(10,[1,3,4,1,3,1]))