'''
사방이 막히면 방 하나
사방이 막혔다는 걸 어떻게 알 수 있을까
사각형 - 상하좌우의 수가 동일해야할거 가ㅏㅌ음
이미 나온 좌표가 또 나오면 방이 생긴거임
1. 좌표를 확인한다
'''

def solution(arrows):
    answer = 0
    coordinate = set()    # 지나간 좌표 확인용
    loc = [0,0]  # x, y  집합 자료형은 인덱스로 접근이 불가

    for direc in arrows:
        loc=list(loc)
        if direc == 0:
            loc[1] += 1
        elif direc == 1:
            loc[0] += 1
            loc[1] += 1
        elif direc == 2:
            loc[0] += 1
        elif direc == 3:
            loc[0] += 1
            loc[1] -= 1
        elif direc == 4:
            loc[1] -= 1
        elif direc == 5:
            loc[0] -= 1
            loc[1] -= 1
        elif direc == 6:
            loc[0] -= 1
        else:
            loc[0]-=1
            loc[1]+=1
        loc = tuple(loc)
        if loc in coordinate:
            answer += 1

        coordinate.add(loc)

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
