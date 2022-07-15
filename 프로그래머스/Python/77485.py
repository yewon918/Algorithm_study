'''
rows x columns, 회전들의 목록 queries 주어짐
시계방향으로 회전, 정수 4개로 표현
회전들을 배열에 적용, 위치가 바뀐 숫자 중 작은 숫자 순서대로 배열에 -> return
----
회전하는 숫자들을 어떻게 잡아줘야하지?
배열 4개 생성
2 2 5 4
x1~y1 / y1~y2 / x2~y2 / x1~x2
2~2/ 2~4/ 2~4/ 2~5
'''
from collections import deque
def solution(rows, columns, queries):
    answer = []
    map = []
    deq = deque()

    cnt = 1
    for i in range(rows):
        map.append([])
        for j in range(columns):
            map[i].append(cnt)
            cnt += 1

    min_v=[]
    for q in queries:
        x1, y1, x2, y2 = q

        for k in range(y2-y1):
            deq.append(map[x1-1][y1-1+k])

        for a in range(x2-x1):
            deq.append(map[x1-1+a][y2-1])

        for k in range(y2-y1):
            deq.append(map[x2-1][y2-1-k])

        for a in range(x2-x1):
            deq.append(map[x2-1-a][y1-1])

        print(deq)


        min_v.append(min(deq))
        tmp = deq.pop()
        deq.appendleft(tmp)
        print(deq)

        c = 0
        for k in range(0, y2-y1):  # 2칸만
            map[x1-1][y1-1+k] = deq[k]
            c+=1

        for a in range(c, c+x2-x1):  # 3칸만
            map[x1-1+a][y2-1] = deq[a-1]    # c+a라고 해버리니까 3, 5, 7 이렇게 감..
            c+=1
            print('x축', x1-1+a, 'y축', y2-1)
        for k in range(0, y2-y1):  # 2칸만
            map[x2-1][y2-1-k] = deq[c+k]
            c+=1
        print(map)
        for a in range(0, x2-x1):   # 3칸
            map[x2-1-a][y1-1] = deq[c+a]
            c+=1

        print(map)
        print(min_v)

        break


    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))