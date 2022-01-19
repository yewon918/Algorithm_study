"""
k개의 수를 제거해서 가장 큰 수
재귀함수 - 함수 인덱스로 -를 넘겨줌

"""

def calc(cnum, k, i):
    global store

    if k == 0:
        if store < int(str(cnum)):
            store = int(str(cnum))
        return

    k-=1

    del cnum[i]
    for j in range(0,len(cnum)):
        calc(cnum, k, j)
    # 리스트의 인덱스를 하나씩 움직이며 값을 지워나감


def solution(number, k):
    answer = ''
    global store
    store = -1

    lnum = list(number)
    i=0
    calc(lnum, k, i)

    answer = store
    return str(answer)

print(solution(number="1924", k=2))