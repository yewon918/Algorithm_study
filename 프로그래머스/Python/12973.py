'''
알파벳 소문자 문자열 - 2개씩 붙어 있는 짝
-> 둘 제거, 나머지 문자열 이어 붙임
-> 모두 제거 -> 짝지어 제거하기 성공할 수 있는지
성공적 수행- 1, 아님- 0
----
반복문: 인덱스 비교해서 붙어있는거 찾기 (len s -1 만큼 돌리기)
찾으면 해당 부분 삭제 -> 확인요망
# 1차 - 35분

'''
def solution(s) :
    stack = []

    for a in s:
        if not stack:   # 비었다면
            stack.append(a)
        elif stack[-1] == a:    # stack의 맨 위가 동일하다면
            stack.pop()
        else:
            stack.append(a)
    if stack:
        return 0
    else: return 1

print(solution(s='cdcd'))