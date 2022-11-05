'''
자연수 N - 숫자 재배열, N보다 큰 N의 배수 만들 수 있는지


'''
import sys
sys.stdin = open("input.txt", "r")

from itertools import permutations

T = int(input())
for i in range(1, T+1):
    data = list(map(int, input()))
    original = int(''.join(map(str, data)))

    result = 'impossible'
    for value in permutations(data, len(data)):
        if int(''.join(map(str, value))) > original:
            if int(''.join(map(str, value))) % original:
                result = 'possible'
                break
    print('#%d %s' %(i, result))