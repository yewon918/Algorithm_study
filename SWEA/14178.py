'''
좌표에 꽃이 하나씩 - N개 좌표, N개의 꽃
x에 분무기 -> [x-D, x+D1] 모든 꽃들
모든 꽃이 한개 이상의 물을 받을 수 있도록 하는 최소한의 분무기 수

    
ㅁㅁㅁ|ㅁ|ㅁㅁㅁ
x-3~x+3

입력된 수 * 2+1만큼 커버 가능
100 / 7 = 15 올림?
5 / 3 = 1 ... 1
5 / 5 = 1
'''
import sys
sys.stdin = open("14178.txt", "r")

T = int(input())
for i in range(T):      # 테스트케이스만큼 반복
    N, x = map(int, input().split())
    calc = x*2+1

    answer = N // calc
    rest = N % calc

    if rest >= 1:
        answer += 1

    print('#{} {}'.format(i+1, answer))

