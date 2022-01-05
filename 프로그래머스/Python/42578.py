def solution(clothes):
    mul = 1
    answer = 0
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 1   # 추가
        else:
            dict[i[1]] += 1


    for j in dict:
        mul *= (dict.get(j) + 1)

    answer = mul - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
