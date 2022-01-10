'''
2 이상 중복의 경우 숫자로 표현, 1은 숫자 없음
2개 단위로 자르기
문자열 압축한 것 중 가장 짧은 것의 길이 return
'''
"""
for i in range(len(문자열))
정해진 길이만큼 잘라야한다.
문자열 mod i == 0인 경우만 가능

[0:i]로 잘라서 list에 넣기
다 list.append()해서 넣고, 

list 맨 앞 원소 기준으로 바로 뒤 원소가 같으면 세어주면서 삭제
같은게 있었다면, tmp += 해당 원소 길이 + 1
같은게 없었다면 tmp += 해당원소 길이
이후 candi.append(tmp)
tmp = 0

각 문자 요소가 뒤에 있는지 없는지 판단?
"""
from collections import deque
def solution(s):
    answer = 0
    sliced=deque([])
    candi = []
# 0~14
# 1로 한바퀴 다 돌고 그 다음 바퀴 돌도록
    for i in range(len(s)):
        copy = list(s)
        if i == 0 or len(s) % i != 0:
            continue
        while copy:
            check = copy[:i]
            if i == 1:          # 뒤에 같은 문자가 없으면 종료
                if check not in s:
                    answer = len(s)
                    return answer
            sliced.append(copy[:i])     # i만큼 자른 거 list에 넣기
            copy.lstrip(copy[:i])       # 어떻게 하는거지..?
    tmp = 0
    front = sliced.popleft()
    while sliced:
        second = sliced.popleft()
        n = len(front)
        if front == second:      # 앞뒤 원소가 같다면,
            n += 1
        tmp += n
        front = second
    candi.append(tmp)

    answer = min(candi)
    return answer

s = "aabbaccc"
print(solution(s))




