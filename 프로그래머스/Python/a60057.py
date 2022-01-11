def solution(s):
    answer = len(s)
    candi = ""

    for i in range(1, len(s) // 2 + 1):     # 토큰의 길이 설정
        front = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if front == s[j:j+i]:           # 그 다음과 같을 경우
                cnt += 1
            else:                           # 같지 않음, 비교 끝
                if cnt >= 2:                # 중복의 경우가 2 이상
                  candi += str(cnt) + front     # 숫자와 함께 넣어줌
                else:
                    candi += front
                front = s[j:j+i]    # 그 다음 토큰
                cnt = 1
        if cnt >= 2:
            candi += str(cnt) + front
        else:
            candi += front

        answer = min(len(candi), answer)
    return answer

s = "aabbaccc"
print(solution(s))