'''
10시 15분까지
맨 처음에 A로만 이루어짐
최소 이동 구하기

아스키로 해당 문자가 A에서 몇 차이 나는지 확인
전부 ^로 하는 경우, ^에서 >하는 경우, 전부 고려
26이상이면 거꾸로 (<)

'''

def solution(name):
    answer = 0
    # 위 아래를 센다
    up_down=[min(ord(i)-ord("A"), ord("Z")-ord(i)+1) for i in name]
    idx = 0
    # 좌우 어느 쪽으로 이동하는게 나을 지 센다
    while True:
        answer += up_down[idx]
        up_down[idx]=0

        if sum(up_down) == 0:
            break

        right = 1
        left = 1
        while up_down[idx+right] == 0:
            right += 1
        while up_down[idx-left] == 0:
            left += 1

        # 어느 쪽으로 이동하는 것이 현명한지 판단
        if right <= left:   # 같으면 상관없음
            idx += right
            answer += right
        else:
            idx += -left        # 주의
            answer += left

    return answer

print(solution("JEROEN"))