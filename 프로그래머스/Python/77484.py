'''
44 1  0  0 31 25
31 10 45 1 6 19
최고 순위 - 일치하는거 + 0 개수
최저 순위 - 일치하는 것만
:개수 맞게 순위 정리
'''
def check(check):
    if check == 6: return 1
    elif check == 5: return 2
    elif check == 4: return 3
    elif check == 3: return 4
    elif check == 2: return 5
    else: return 6

def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
            continue
        if i in win_nums:
            correct += 1

    best = zero + correct
    # worst = correct

    answer.append(check(best))
    answer.append(check(correct))

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))