'''
비어있음 .
막혀있음 #
막혀있는 칸들이 하나의 정사각형을 이루는지? yes/ no
----
https://unie2.tistory.com/1110
'''
import sys
sys.stdin = open("input.txt", "r")

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



    print(tmap)
