'''
멈춘 위치에서 가장 위에 있는 인형 집어올림
-> 바구니 아래부터 쌓임
같은 인형 두개 - 터짐
1~100 숫자 - 다른 모양의 인형
0 - 빈칸
return 사라진 인형
----
입력 배열 처리 - 인덱스로 세고
0이면 그 다음 row
0이 아니면 pop 해서 바구니에 넣고 바구니에서 같으면 세기
'''
from collections import deque
def solution(board, moves):
    answer = 0
    basket = deque([])

    for loc in moves:
        for row in board:
            if row[loc-1] == 0:
                continue
            else:
                basket.append(row[loc-1])   # 0으로 만들기
                row[loc-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        answer += 2
                        basket.pop()
                        basket.pop()
                break
    return answer

print(solution(board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves = [1,5,3,5,1,2,1,4]))