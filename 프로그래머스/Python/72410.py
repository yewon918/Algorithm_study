'''
3-15
소문자, 숫자, -, _, .(처음 끝 안됨, 연속 사용 불가)

소문자 만들기
안되는거 제거하기
..이상 연속이면 .로
빈문자면 a
---
0) 빈문자열인지 판단 비었다면 aaa, 2 이하면 반복
1) 대문자 판별하면서-> 소문자로 전부 바꿔주기
2) 이상한 문자 제거, . 반복은 하나로, . 위치 확인(처음, 끝 제거)
3) 15개로 잘라내고 끝에 . 제거


'''
from collections import deque

def solution(new_id):
    answer = ''
    avaliable = ['.','-','_']
    l = len(new_id)

    if len(new_id) == 0:
        answer='aaa'
        return answer

    new_id = new_id.lower()     # 1단계 - 소문자 변환

    new_id = deque(new_id)
    for c in range(l):          # 2단계 - 특수문자 확인
        c = new_id.popleft()
        if c.isalnum() or c in avaliable:
            new_id.append(c)

    cnt = 0                     # 3단계 . 치환
    for check in range(len(new_id)):
        check = new_id.popleft()
        if check == '.':
            cnt += 1
            if cnt > 1: continue
        else:
            cnt = 0
        new_id.append(check)


    if new_id[0] == '.':        # 4단계 처음, 뒤 . 확인
        del new_id[0]
    if len(new_id)>0 and new_id[-1] == '.':
        new_id.pop()

    # if len(new_id) > 15:
    #     new_id = itertools.islice(new_id, 0, 15)
        # deque 인덱스 슬라이싱 하려면 안됨, islice사용 이후 del 사용이 또 안됨


    if len(new_id) == 0:         # 5단계 a 대입
        new_id.append('a')

    if len(new_id) > 15:    # 6단계 - 길이 줄이기, 끝 확인인
        tmp = "".join(new_id)
        new_id = deque(tmp[:15])
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id.pop()

    if len(new_id) <= 2:    # 7단계 - 3될 때까지 반복
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    answer = "".join(new_id)
    return answer

print(solution("....."))