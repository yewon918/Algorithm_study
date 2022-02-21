'''
rocks에서 n개 뽑아서 없애야함
바위 sort
그 다음수가 앞 수를 빼줌
거리 최솟값 기록
'''

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance

    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed_rocks = 0

        for rock in rocks:
            if rock - current < mid:
                removed_rocks += 1
            else:
                current = rock
        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

print(solution(25,[2, 14, 11, 21, 17],2))