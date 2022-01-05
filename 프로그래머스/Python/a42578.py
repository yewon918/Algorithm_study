def solution(clothes):
    answer = 1
    dic = dict()

    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for val in dic.values():
        answer *= (val + 1) # 아무것도 안입을 경우 생각해서 + 1
    return answer - 1
# 아무것도 안입진 않으니까 -1
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))