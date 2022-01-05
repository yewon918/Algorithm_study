from itertools import permutations

def check(x):
    if x < 2:
        return False
    for i in range(2, x):   # 2 ~ x-1
        if x % i == 0:
            return False
        return True         # 조건 성립

def solution(numbers):
    answer = []
    per = []
    for i in range(1, len(numbers)+1):      # 1 ~ num
        per = list(map(''.join, permutations(numbers, i)))      # 순열의 결과를 합침  --> 310
        per = set(per)          # 집합자료형  -> 중복제거 해서 개별로 분리
        for p in per:           # 집합자료형 하나씩 비교
            if check(int(p)):
                answer.append(int(p))   # 조건 성립시 answer에 넣음
    answer = set(answer)        # 중복 제거
    return len(answer)


numbers = "011"
print(solution(numbers))
