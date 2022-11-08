'''
비어있음 .
막혀있음 #
막혀있는 칸들이 하나의 정사각형을 이루는지? yes/ no
----
https://unie2.tistory.com/1110
'''
import sys
sys.stdin = open("input.txt", "r")

'''
T = int(input())
for i in range(1, T+1):
    size = int(input())
    tmap = [list(input().split()) for s in range(size)]
    # tmap = []
    # for k in range(size):
    #     tmap.append(list(input().split()))
    first = (21,21)
    last = (21,21)
    tmp = 'yes'
    for row in range(size):
        for col in range(size):     # 한줄 완성하고
            if tmap[row][col] == '#':
                if first == (21, 21):
                    first = (row, col)
                    break
                if first != (21, 21) and last == (21, 21):  # last 지정
                    last = (row, col)
        for search in range(0, size):
            if tmap[search][size] != '#':
                tmp = 'no'
                break
        for search2 in range(0, size):
            if tmap[size][search2] != '#':
                tmp = 'no'
                break
'''

    
t = int(input())

def check(board, cnt, n):
    for i in range(n):
        for j in range(n):
            
            if board[i][j] == 1:
                col = 0
                row = 0
                
                for k in range(i+1, n): # i+1을 하면 횟수 몇번 줄인다.
                    if board[k][j] == 1:
                        col += 1
                    else: break
                    
                for l in range(j+1, n):
                    if board[i][l] == 1:
                        row += 1
                    else: break
                
                if row != col: 
                    return 'no'                        
                
                for a in range(i, i+col+1):
                    for b in range(j, j+row+1):
                        if board[a][b] == 1: 
                            cnt -=1
                        else:
                            return 'no'
                        
                if cnt != 0: 
                    return 'no'
                
                return 'yes'


for tc in range(1, t+1):
    n = int(input())
    board = [[0 for i in range(n)] for j in range(n)]
    
    cnt = 0
    for i in range(n):
        data = list(map(str, input()))
        for j in range(n):
            if data[j] == '#':
                board[i][j] = 1
                cnt +=1
        
    result = check(board, cnt, n)        
    
    print('#%d %s' %(tc, result))

