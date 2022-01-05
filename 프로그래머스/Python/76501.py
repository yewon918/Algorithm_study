absolutes = [4,7,12]
signs = [True, False, True]

def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
        answer += absolutes[i]


    return answer

print(solution(absolutes, signs))
