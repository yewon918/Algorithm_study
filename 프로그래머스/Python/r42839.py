from itertools import permutations

def check(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    per = []        # 중복제거, 확인용
    for i in range(1, len(numbers)+1):  # r에 들어갈 수 정하는 중
        per = list(map(''.join, permutations(numbers, i)))
        per = set(per)
        for j in per:
            if check(int(j)):
                answer.append(int(j))

    answer = set(answer)  # answer중에 중복제거를 수행해야함
    return len(answer)

numbers = "011"
print(solution(numbers))
