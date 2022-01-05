'''
n개의 음이 아닌 정수 +, -로 타겟넘버 만들기
사용가능 숫자 담긴 배열 numbers, 타겟넘버 target
'''


# answer = 0
# def dfs(numbers, idx, total, target):
#     global answer
#     if idx == len(numbers):
#         if total == target:
#             answer += 1
#         return
#     dfs(numbers, idx+1, total+numbers[idx], target)
#     dfs(numbers, idx+1, total-numbers[idx], target)


# def solution(numbers, target):
#     global answer

#     dfs(numbers, 0, 0, target)
#     return answer


# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target))


def solution(numbers, target):
    answer = 0
    tmp = [0]
    result = []

    for i in numbers:
        for j in tmp:
            tmp.append(tmp[j] + numbers[i])
            tmp.append(tmp[j] - numbers[i])
        result = tmp

    return result.count(target)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
