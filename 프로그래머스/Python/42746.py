'''
combination 활용해서 그 중 max 구하기

'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

numbers = [6, 10, 2]
print(solution(numbers))

