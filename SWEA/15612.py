'''
8x8 체스판
0~64개의 룩
- 정확히 8개의 룩
- 같은 열이나 행에 있으면 안됨
---
어제 푼거랑 동일한 양상.
룩 위치마다 각각 열, 행만 조사하면 될거 같다. 

'''

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for case in range(1, t+1):
    rook = 0
    blist = [input() for _ in range(8)]
    answer = 'yes'
    
    for x in range(0, 8):
        for y in range(0, 8):
            if blist[x][y] == 'O':      # rook 발견
                cx = 0
                cy = 0                  # 해당 스팟부터 확인한다.
                for check in range(y, 8):     # row 확인
                    if blist[x][check] == 'O':
                        cx += 1
                for check in range(x, 8):
                    if blist[check][y] == 'O':
                        cy += 1
                if cx > 1 or cy > 1:
                    answer = 'no'
                    break
        if answer == 'no':
            break
    
    for i in range(8):
        rook += blist[i].count('O')
    
    if rook != 8: 
        answer = 'no'

    print('#{} {}'.format(case, answer))