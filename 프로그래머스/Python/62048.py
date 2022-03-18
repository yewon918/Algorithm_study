'''
크기가 같은 직각삼각형 2개 - 이 상타에서 가로세로 1cm 잘라서 사용
-----
대각선이 가로질러 가는 모양은 동일할 것

'''
import math
def solution(w,h):
    answer = 1

    gcd = 1
    small = w if w < h else h
    for i in range(1, small+1):
        if w % i == 0 and h % i == 0:
            gcd = i     # 최대공약수를 찾는다

    answer = w*h - (w//gcd + h//gcd-1)*gcd

    return answer

print(solution(8,12))