'''
n미터 통나무 자르는 게임
alice 시작. 번갈아가면서 자름. 
두 조각으로 나눔, 자연수의 길이 가짐, 더이상 자를 수 없을때 짐
-----
남은 길이 모두가 1이면, 1보다 작을 예정이면 패배
횟수가 짝수면 bob 승리
3 -> a: 1|2 -> b: 1|1|1
10 -> a: 5 | 5 -> b: 2| 3| 2| 3 -> a: 1|1|1|2|1|1|1|2
자를게 없으면 이기는건가
/2 했을때 나머지 있으면 bob, 없으면 alice? -> 아님
'''

import sys
sys.stdin = open('input.txt','r')

t = int(input())

for tc in range(1, t+1):
    wood = int(input())
    if wood % 2 == 1:
        answer = "Bob"
    else:
        answer = "Alice"
    print("#{} {}".format(tc, answer))
    