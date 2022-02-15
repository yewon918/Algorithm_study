'''
이중우선순위 큐
operations - 큐 연산
최대, 최솟값이 두인 경우 하나만 삭제
빈 큐에서 삭제 연산 -> 무시

문자열을 입력받고, 뒷글자를 슷자로 바꿔주는 과정이 필요
띄어쓰기 기준으로 인덱스 슬라이싱 : a.split()


'''

def solution(operations):
    answer = []
    arr = []
    for op in operations:
        op = op.split()
        num = int(op[1])        # append할 대상입니다.

        if op[0] == 'I':
            arr.append(num)
        else:       # D인 경우
            if len(arr) <= 0: continue       # 다음 반복
            if num == 1:      # 1인 경우 최댓값 삭제
                tmp = max(arr)
            else:               # -1인 경우 최솟값 삭제
                tmp = min(arr)
            arr.remove(tmp)

    # print(arr)

    if not arr:     # 비었음
        answer.extend([0,0])
    else:
        maxi = max(arr)
        mini = min(arr)
        answer.extend([int(maxi), int(mini)])

    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))