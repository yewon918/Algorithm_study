'''
1차원 정수 배열 a,b가 매개변수로 주어짐

'''
def solution(a, b):
    answer = 1234567890

    answer = 0
    while a:
        answer += a.pop() * b.pop()

    return answer

print(solution([-1,0,1],[1,0,-1]))