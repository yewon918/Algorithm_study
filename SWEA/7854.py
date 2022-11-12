'''
특별한 성질을 가지는 약수 - 최약수
최약수의 종류. 숫자 x보다 작거나 같은 최약수 개수
최약수: 자기자신 포함
앞에 어떤 수를 붙여도 자신을 약수로 - 
for i in 해당수:
    i 보다 큰 ~ 해당수보다 작은 -> 전부 나눠보며 확인
--> 시간 걸릴거 같은데..?

점화식이 필요하다.

---
10 안에서 계산을 먼저 해보자
'''
import sys
sys.stdin = open('input.txt','r')

t = int(input())
for tc in range(1, 2):
    # num = int(input())
    # cnt = 0
    
    # for i in range(1, num):
    #     for j in range(i, num):
    #         if j >= i and j%i==0:
    #             cnt += 1
    #         else: continue
            
    # print('#{} {}'.format(tc, cnt))
    
    for i in range(1, 11):
        nn = 10+i
        # print(nn)
        if nn % i == 0:
            print(i)