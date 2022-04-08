def solution(key, lock):
    answer = False
    N = len(key)
    M = len(lock)

    newarray = [[0]*(M*3) for _ in range(M*3)]

    # 3배 확장된 new array(lock)를 만든다.
    for i in range(M):
        for j in range(M):
            newarray[i + M][j + M] = lock[i][j]

    for k in range(4):      # 4번 돌린다
        key = rotated(key)
        for a in range(1, M*2):         # 범위: 1 ~ M*2-1
            for b in range(1, M*2):

                for i in range(N):      # key의 인덱스
                    for j in range(N):
                        newarray[a+i][b+j] += key[i][j]

                if check(newarray) == True: # 맞음
                    return True
                else:
                    for i in range(N):
                        for j in range(N):
                            newarray[a+i][b+j] -= key[i][j]

    return answer


def rotated(key):
    rkey = [[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            rkey[j][len(key)-i-1] = key[i][j]
    return rkey


def check(arr):
    size = len(arr)//3     # 중간만 확인
    for i in range(size, size*2):
        for j in range(size, size*2):
            if arr[i][j] != 1: return False
    return True
